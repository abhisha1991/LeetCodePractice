# https://www.notion.so/Your-First-DAG-in-5-minutes-5d15bb2c51b044ea9b8266b2ac07c1fe
# https://marclamberti.com/blog/airflow-dag-creating-your-first-dag-in-5-minutes/

from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from random import randint

 default_args={
            "owner": "airflow",
            "retries": 1,
            "retry_delay": timedelta(minutes=5),
            "start_date": datetime(2022, 3, 9),
        }

def _choose_best_model(ti):
    # ti stands for task instance. This is part of the context object 
    # this object cannot grow indefinitely, so it should not be used as a data processing pipeline for huge data transfers
    # typically based on which db (mysql, postgres, sqlite) -- are backing this context object, we see a max size of 2 GB
    # xcom_pull and xcom_push are ways to pass around data from function to function
    accuracies = ti.xcom_pull(task_ids=['model1', 'model2', 'model3'])
    maxacc = max(accuracies)
    # the returned values are passed down from this function to the next function in the workflow
    # if you look at the diagram below, the results from this function feeds into accurate/inaccurate functions
    # notice here, we are just returning the "task_id" for the downstream execution path
    if maxacc > 8:
        return 'accurate'
    return 'inaccurate'

def _model():
    # simulation of returning accuracy
    # the returned values are passed down from this function to the next function in the workflow
    # if you look at the diagram below, the results from model feeds into choose_best_model
    return randint(1, 10)

# configure custom schedule intervals: https://airflow.apache.org/docs/apache-airflow/1.10.1/scheduler.html#dag-runs
# use schedule_interval=None and not schedule_interval='None' when you don’t want to schedule your DAG
# can have other key words below like: @hourly, @weekly, @monthly, @yearly, @once -- which will schedule at the beginning of the corresponding time period 
with DAG(dag_id="first_dag", schedule_interval="@daily", default_args=default_args, catchup=False) as dag:

    model1 = PythonOperator(
        task_id = 'model1',
        python_callable = _model
    )

    model2 = PythonOperator(
        task_id = 'model2',
        python_callable = _model
    )

    model3 = PythonOperator(
        task_id = 'model3',
        python_callable = _model
    )

    choose_best_model = BranchPythonOperator(
        task_id = 'choose_best_model',
        python_callable = _choose_best_model
    )

    accurate = BashOperator(
        task_id = 'accurate',
        bash_command = "echo 'accurate'" # since this is part of bash operator, this bash command gets executed, when this task is called
    )

    inaccurate = BashOperator(
        task_id = 'inaccurate',
        bash_command = "echo 'inaccurate'"
    )

    # remember to set up the dependencies!
    [model1, model2, model3] >> choose_best_model >> [accurate, inaccurate]

    '''
    model1                       accurate
          \                     /
    model2 --- choose_best_model
           /                    \
    model3                       inaccurate

    if it was a singular flow without branching, you would just do something like (without lists)
    func1 >> func2 >> func3
    '''

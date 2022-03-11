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

# notice how we're passing the context object here, which is possible because we set provide_context in the respective functions
def func1(**context):
    # this is a preferred way to param pass since its more explicit and you have control over key names
    # always a good idea to prepend the name before the key name to avoid key collisions in the ti dictionary
    context.get("ti").xcom_push(key="{}_key1".format(func1.__name__), value=123)

def func2(**context):
    val = context.get("ti").xcom_pull(key="{}_key1".format(func1.__name__))
    return val

with DAG(dag_id="second_dag_passing_params", schedule_interval="@daily", default_args=default_args, catchup=False) as dag:
    func1 = PythonOperator(
        task_id = 'func1',
        python_callable = func1,
        provide_context = True # this allows us to pass the context object around between functions
        op_kwargs = {"name": "abhisha"} # allows to pass function values via the kwargs argument available in the function
    )

    func2 = PythonOperator(
        task_id = 'func2',
        python_callable = func2,
        provide_context = True
    )

    func1 >> func2


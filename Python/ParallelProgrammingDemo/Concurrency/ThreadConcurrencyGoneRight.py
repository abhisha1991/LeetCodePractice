# https://www.youtube.com/watch?v=bs9tlDFWWdQ
# approx 4 mins into the vid, he talks about concurrency with threading 
import threading
import time
counter = 0
lock = threading.RLock()

def func1():
    global counter

    while True:
        with lock:
            counter +=1
            print(f"From func1 post increment: {counter}")            
            counter -=1
            print(f"From func1 post decrement: {counter}")
            time.sleep(2)      

def func2():
    global counter

    while True:
        with lock:
            counter +=1
            print(f"From func2 post increment: {counter}")            
            counter -=1
            print(f"From func2 post decrement: {counter}")
            time.sleep(1)

# here is how we can achieve concurrency -- via locks in threading
threading.Thread(target=func1).start()
threading.Thread(target=func2).start()

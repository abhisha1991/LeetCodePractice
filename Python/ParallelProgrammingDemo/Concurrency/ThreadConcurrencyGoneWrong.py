# https://www.youtube.com/watch?v=bs9tlDFWWdQ
# approx 3 mins into the vid, he talks about why the below is a bad idea
# goal is to increment and decrement a global variable, such that its value is 0 guaranteed at any point of observation

import threading
import time
counter = 0

def func1():
    global counter

    while True:
            counter +=1
            counter -=1

def func2():
    global counter

    while True:
            counter +=1
            counter -=1

def func_print():
    global counter
    while True:
            print(counter)

# here we have no locks, so we cannot guarantee that the counter values will on average be 0 after every call
# they can be anything depending on what thread got access to them based on the CPU scheduler giving a favorable thread access.

# say thread 1 is hosting func1 and thread 2 is hosting func2
# now say that we came into thread1 (CPU gave thread1 access first), then on line 13, we increment counter to 1
# now say that while counter was being incremented, CPU scheduler decides to give access to thread2
# now we may again increment counter to 2 (line 20) before func1 has a chance to decrement on line 14 when it gets back execution control
# from the scheduler. Now at this point, if we print, we will observe a value of 2 - which isn't what we intended!

# NOTE THAT THREADS CAN BE PRE-EMPTED BY SCHEDULER AT ANY POINT, IT IS NOT NECESSARY THAT A FUNCTION/CYCLE MUST COMPLETE IN A THREAD 
# BEFORE CONTROL IS GIVEN TO ANOTHER THREAD BY THE SCHEDULER

# ITS ENTIRELY POSSIBLE THAT ONLY A SINGLE LINE OF A FUNCTION IS EXECUTED IN A THREAD, BEFORE THE SCHEDULER PRE-EMPTS THAT THREAD 
# AND TAKES CONTROL AWAY
threading.Thread(target=func1).start()
threading.Thread(target=func2).start()
threading.Thread(target=func_print).start()
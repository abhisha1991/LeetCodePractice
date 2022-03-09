'''
# https://www.youtube.com/watch?v=fKl2JW_qrso
A multiprocessing system has more than two processors, 
whereas Multithreading is a program execution technique that allows a single process to have multiple code segments
'''
import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # processes end up using all the cores available to them
    results = executor.map(do_something, secs)

    # since we're getting back a string from the function, we can access it from results like so
    for r in results:
        print(r)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
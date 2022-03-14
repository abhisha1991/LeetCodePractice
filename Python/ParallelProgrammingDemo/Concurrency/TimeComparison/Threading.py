# https://www.youtube.com/watch?v=R4Oz8JUuM4s
# https://github.com/nikhilkumarsingh/async-http-requests-tut

import requests
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import Pool
import asyncio
import aiohttp
import time

from timer import timer

URL = 'https://httpbin.org/uuid'


def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])

# threading
# note that there can only be 1 thread run at a time in a python interpreter, due to GIL
# we cannot parallelize in the case of multithreading due to GIL, 
# but we can leave it up to context switching done by the OS/library frameworks 'concurrent.futures' to help us get a boost in speed.
# note that thread execution is "stopped" or pre-empted by another thread, and that is decided by the scheduler/os/framework -- and programmer has no control over this.
# we have to be careful about the max_workers argument, if too many, it could lead too too much context switching, thus increasing overall time

# threads are segments of a process and are more light weight compared to process, thus we expect a speedup - there is less overhead setting up a thread
print("Threading start:")
start = time.time()
with ThreadPoolExecutor(max_workers=100) as executor:
        with requests.Session() as session:
            executor.map(fetch, [session] * 100, [URL] * 100)
            executor.shutdown(wait=True)

end_thread = time.time() - start

print(f"Threading ended, taking total time (sec): {end_thread}")

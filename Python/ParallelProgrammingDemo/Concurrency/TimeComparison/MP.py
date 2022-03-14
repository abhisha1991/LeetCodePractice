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

# multi processing
# one process executes on 1 core of a machine, so a multicore machine can run many processes in parallel
# there is some overhead in setting up the processes, so while there is parallelism, it may not be super fast
print("MP start:")
start = time.time()
with Pool() as pool:
        with requests.Session() as session:
            pool.starmap(fetch, [(session, URL) for _ in range(100)])

end_process = time.time() - start

print(f"MP ended, taking total time (sec): {end_process}")
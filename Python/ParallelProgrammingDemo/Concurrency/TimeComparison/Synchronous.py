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

# synchronous
print("Synchronous start:")
start = time.time()
with requests.Session() as session:
    for _ in range(100):
        fetch(session, URL)

end_sync = time.time() - start

print(f"Synchronous ended, taking total time (sec): {end_sync}")
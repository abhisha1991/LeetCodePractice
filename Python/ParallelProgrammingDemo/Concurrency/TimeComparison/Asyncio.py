# https://www.youtube.com/watch?v=R4Oz8JUuM4s
# https://github.com/nikhilkumarsingh/async-http-requests-tut
'''
A coroutine is a special function that can give up control to its caller without losing its state. 
A coroutine is a consumer and an extension of a generator. One of their big benefits over threads is that they dont use very much memory to execute. 
Note that when you call a coroutine function, it doesnt actually execute. 
Instead it will return a coroutine object that you can pass to the event loop to have it executed either immediately or later on.
'''
import requests
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import Pool
import asyncio
import aiohttp
import time

from timer import timer

URL = 'https://httpbin.org/uuid'

async def fetch_async(session, url):
    async with session.get(url) as response:
        x = await response.json()
        print(x['uuid'])

# async io
# runs in a single global event loop, notice there's no "async functionality inherent about these get http calls" 
# there's hardly anything blocking here, esp in this API -- which is just a dummy api
# however, imagine if the api was going to take a lot of time (say provision a vm), and as a result could be "blocking" - then this asyncio lib would be useful
# async/await allows the individual client calls to "give back" control to the main event loop, allowing the other tasks in the single global event loop to execute
print("Asyncio start:")
start = time.time()

async def main(loop):
    # notice how the with context also has async wrapped around it
    async with aiohttp.ClientSession(loop=loop) as session:
        tasks = [fetch_async(session, URL) for _ in range(100)]
        # the * below is just referring to an arbitrary number of arguments, which are not known ahead of time
        # else the syntax of gather is something like gather(func1(), func2()....)
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))

end_asyncio = time.time() - start

print(f"Asyncio ended, taking total time (sec): {end_asyncio}")

import asyncio
import time

# global variable
counter_for_async_io  = 0
counter_for_thread = 0

async def func1_async():
    global counter_for_async_io

    while True:
        counter_for_async_io +=1
        print(f"From func1_async post increment: {counter_for_async_io}")
        counter_for_async_io -=1
        print(f"From func1_async post decrement: {counter_for_async_io}")
        # meaning of await keyword is "its fine now to go from this function to another - 'Im releasing my lock'""
        # so we are in control on when we need to do context switching
        # context switch only happens after calling await
        # and that's exactly what we want as programmers
        # in short -- await is a checkpoint where it is safe for asyncio to go to another coroutine (function)
        
        # its a good idea to await calls that are going to take time, ex. fetching data from a network call
        # at that point, we know we're going to take a while and we want ourselves to execute in the background
        # so transfer control (main thread) back over to someone else
        await asyncio.sleep(1)

async def func2_async():
    global counter_for_async_io

    while True:
        counter_for_async_io +=1
        print(f"From func2_async post increment: {counter_for_async_io}")
        counter_for_async_io -=1
        print(f"From func2_async post decrement: {counter_for_async_io}")
        await asyncio.sleep(1)

# notice that the output of this would look something like
'''
From func1_async post increment: 1
From func1_async post decrement: 0
From func2_async post increment: 1
From func2_async post decrement: 0
....
This pattern is determinsitic, which is a good thing!
'''
# gather declares all the async functions you want to register up front into the event loop
asyncio.gather(func1_async(), func2_async())
asyncio.get_event_loop().run_forever()

'''
Asyncio is an abstraction over "the event loop" 
There is a "single" large infinite loop running in the background as shown in the last line of the program above, "which runs forever"
The different await calls are registered as events in this event loop 

For example, say you await a networking call to fetch some data -- when the network call finishes, an "event has occurred"
x = await network_call(url)
Until the point when the network call has finished, no event has occurred for us, 
and the event loop will iterate over other awaited calls to see if they finished first and address them if they finished before us.

At some point shortly after the network call is finished, the event loop will reach "our code" and assign the network call result to x.
'''

'''
If you cannot use gather to declaritively say which functions you want to have in your event loop, you can start individual tasks too
async def get_users():
    users = await client.get_all_users()
    return users

async def main():
    task = asyncio.create_task(get_users())
    await task

asyncio.run(main())
'''

'''
async def main():
    await asyncio.get_event_loop().run_in_executor(None, some_expensive_function)

asyncio.run(main())

you may want to do this in cases where you dont want to block the main program thread and 
instead have the expensive func be done asynchronously in another background thread handled by the executor
'''
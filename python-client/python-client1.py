import asyncio
from aiohttp import ClientSession
import time
from matplotlib import pyplot as plt

res_time = []
s = time.monotonic()
async def fetch(url, session):
    start = time.monotonic()
    async with session.get(url) as response:
        end = round(time.monotonic() - start, 4)
        #print("time: {}".format(end))
        res_time.append(end)
        return await response.read()

async def run(r):
    url = "http://3.223.122.238:3000"
    url_palin = "http://3.223.122.238:3000/palindrome/Aiohttp recommends to use ClientSession as primary interface to make requests. ClientSession allows you to store cookies between requests and keeps objects that are common for all requests (event loop, connection and other things). Session needs to be closed after using it, and closing session is another asynchronous operation, this is why you need async with every time you deal with sessions."
    tasks = []

    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(fetch(url, session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        # you now have all response bodies in this variable
        e = round(time.monotonic() - s, 4)
        #print(res_time)
        #print(sum(res_time))
        #print(e)
        plt.plot(res_time)
        plt.show()



def print_responses(result):
    print(res_time)
    print(sum(res_time))

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(40))
loop.run_until_complete(future)
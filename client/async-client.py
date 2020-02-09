import aiohttp
import asyncio
import time

URL = "http://3.223.122.238:3000"
n = 10000


async def fetch_url(client, url, ts, i):
    async with client.get(url) as resp:
        te = time.time()
        #print(i, resp.status, te - ts)
        return (resp.status, te - ts)


async def n_requests(url, n):
    async with aiohttp.ClientSession() as client:
        for i in range(n):
            ts = time.time()
            status, t = await fetch_url(client, url, ts, i)

loop = asyncio.get_event_loop()
loop.run_until_complete(n_requests(URL, n))
import asyncio
import aiofiles
import aiohttp

base_url = 'http://localhost:8000'
HEADERS = {
    'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/45.0.2454.101 Safari/537.36'),
}

async def get_players():

    url = "https://jsonplaceholder.typicode.com/posts/1"

    #print('Sending request')
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS) as resp:
            data = await resp.json()
            #print(data)


loop = asyncio.get_event_loop()

for i in range(100):
    loop.run_until_complete(get_players())
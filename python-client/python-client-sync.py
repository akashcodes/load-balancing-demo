import requests
import time
from matplotlib import pyplot as plt

res_time = []

def fetch(url):
    start = time.monotonic()
    with requests.get(url) as response:
        end = round(time.monotonic() - start, 4)
        #print("time: {}".format(end))
        res_time.append(end)
        return response.text


def run(r):
    url = "http://3.223.122.238:3000"
    url_palin = "http://3.223.122.238:3000/palindrome/Aiohttp recommends to use ClientSession as primary interface to make requests. ClientSession allows you to store cookies between requests and keeps objects that are common for all requests (event loop, connection and other things). Session needs to be closed after using it, and closing session is another asynchronous operation, this is why you need async with every time you deal with sessions."
    tasks = []
    for i in range(r):
        fetch(url)
    plt.plot(res_time)
    plt.show()


run(10)
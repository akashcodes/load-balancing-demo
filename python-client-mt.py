import logging
import requests
from threading import Thread

n = 10000
url = "http://3.223.122.238:8000"
results = [False for i in range(n)]

def fetch(url, results, index):
    try:
        r = requests.get(url)
        logging.info("Requested..." + url)
        if r.status_code == 200:
            results[index] = True
        else:
            results[index] = False
    except Exception as e:
        logging.error(e)
        results[index] = False
    return True

# create list of threads
threads = []

for i in range(n):
    process = Thread(target=fetch, args=[url, results, i])
    process.start()
    threads.append(process)


# We now pause execution on the main thread by 'joining' all of our started threads.
# This ensures that each has finished processing the urls.
for process in threads:
    process.join()


print(sum(results))
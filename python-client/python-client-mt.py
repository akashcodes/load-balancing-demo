import logging
import requests
import time
from matplotlib import pyplot as plt
from threading import Thread
import numpy as np

n = 1000
url = "http://3.223.122.238:8000"
results = [False for i in range(n)]
times = [0 for i in range(n)]

def fetch(url, results, index):
    start = time.monotonic()
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
    #end = round(time.monotonic() - start, 4)
    end = r.elapsed.total_seconds()
    times[index] = end
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
a = np.array(times)
plt.plot(times)
plt.show()
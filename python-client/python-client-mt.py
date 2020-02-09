import logging
import requests
import time
from matplotlib import pyplot as plt
from threading import Thread
import numpy as np
from queue import Queue

MAX_THREADS = 1



num_theads = MAX_THREADS

n = 10

tests = [
    (1, 1),
    (1000, 10),
    (10000, 100),
    (100000, 1000)
]

url = "http://3.223.122.238:3000/dad-joke"


def sample(n, num_theads):
    
    q = Queue(maxsize=0)

    results = [False for i in range(n)]

    times = [0 for i in range(n)]

    for i in range(n):
        q.put(i)


    def fetch(url, results):
        while not q.empty():
            index = q.get()
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
            end = round(time.monotonic() - start, 4)
            #end = r.elapsed.total_seconds()
            times[index] = end
            #print("Process{} completed".format(index))
            q.task_done()
        return True


    for i in range(num_theads):
        logging.debug('Starting thread ', i)
        worker = Thread(target=fetch, args=[url, results])
        worker.setDaemon(True)
        worker.start()


    q.join()
    #return times
    return np.mean(np.array(times))


a =[]
for test in tests:
    print(test)
    r = sample(test[0], test[1])
    print(r)
    a.append(r)
    #a.extend(sample(test[0], test[1]))

a = np.array(a)
plt.plot(a)
plt.show()
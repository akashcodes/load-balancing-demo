import logging
import requests
import time
from threading import Thread
import numpy as np
from queue import Queue
import os



url_normal = "http://ec2-18-212-227-130.compute-1.amazonaws.com/{}"
url_scaling = "http://WebServer-395753930.us-east-1.elb.amazonaws.com/{}"

routes = [
    "",
    "dad-joke",
    "fibo/{}",
    "fetch",
]

OUTPUT_ROOT = "../output/"
#FILE_PATH = os.path.dirname(os.path.abspath(__file__))


def sample(url, n, num_theads):
    
    q = Queue(maxsize=0)

    results = [False for i in range(n)]

    times = [0 for i in range(nr)]

    for i in range(n):
        q.put(i)


    def fetch(url, results):
        while not q.empty():
            index = q.get()
            start = time.monotonic()
            try:
                r = requests.get(url)
                #logging.info("Requested..." + url)
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
        #logging.debug('Starting thread ', i)
        worker = Thread(target=fetch, args=[url, results])
        worker.setDaemon(True)
        worker.start()


    q.join()
    return results, times
    #return np.mean(np.array(times))


if __name__ == "__main__":

    utype = input("""
    Select:
    1 - Load balanced sampling
    2 - Without load balanced sampling
    """)
    utype = int(utype)

    dire = OUTPUT_ROOT+"without load balancing/"

    url = None
    if utype == 1:
        print("Load Balanced Sample")
        dire = OUTPUT_ROOT+"with load balancing/"
        url = url_scaling
    else:
        print("Sampling without load balancing")
        url = url_normal
    

    print("""
        Select route type: 
        0 - GET /
        1 - GET /dad-joke
        2 - GET /fibo/:number
        3 - GET /fetch
    """)

    route = input()
    route = int(route)

    url = url.format(routes[route])

    if route == 2:
        param = input("Input n to find nth fibonacci number.")
        param = int(param)
        url = url.format(param)


    nr = input("Number of requests?")
    nr = int(nr)

    n = input("Number of threads?")
    n = int(n)
    
    s = input("How many times to sample?")
    s = int(s)
    
    fname = input("Enter file name where to save data: ")
    fname = dire+fname
    tests = [
        (nr, n)
    ] * s

    a = []

    sample_time = []
    
    print("Starting... CTRL+C to quit anytime and save readings so far in the file")

    try:
        for sno, test in enumerate(tests):
            st = time.time()
            print("Running sample", sno+1)
            
            r, t = sample(url, test[0], test[1])
            et = time.time()
            print("Time taken - ", et-st)
            print("-------")
            sample_time.append(et-st)
            t = np.mean(np.array(t))
            a.append(t)
            #a.extend(t)
        print("Average response time:", np.mean(np.array(sample_time)))
        np.savetxt(fname, a)
    
    except KeyboardInterrupt as e:
        
        np.savetxt(fname, a)
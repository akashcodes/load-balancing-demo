import matplotlib.pyplot as plt
import numpy as np

OUTPUT_ROOT = "./output/"

if __name__ == "__main__":
    
    utype = input("""
    Select:
    1 - Load balanced sampling
    2 - Load Balancing with auto-scaling
    3 - Without load balanced sampling
    """)
    utype = int(utype)

    dire = OUTPUT_ROOT+"without load balancing/"

    url = None
    if utype == 1:
        print("Load Balanced Sample")
        dire = OUTPUT_ROOT+"with load balancing/"
    elif utype == 2:
        print("Load Balanced Sample")
        dire = OUTPUT_ROOT+"with load balancing autoscaling/"
    else:
        print("Sampling without load balancing")
    
    fname = input("Enter file name from where to load data: ")
    fname = dire+fname

    data = np.loadtxt(fname)
    print(np.mean(data))
    plt.plot(data)
    #plt.show()
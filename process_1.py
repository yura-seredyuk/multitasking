from data_dict import data
import time
import tracemalloc
import logging
from multiprocessing import Pool

def single_function(responses):
    print(f"{time.strftime('%H:%M:%S', time.localtime())}: Task {responses[0]} started.")
    time.sleep(responses[1])
    print(f"{time.strftime('%H:%M:%S', time.localtime())}: Task {responses[0]} finished.")

def pool_hendler(): #pool_hendler
    p = Pool()
    p.map(single_function, data)

# -----------------------------------
if __name__ == "__main__":
    tracemalloc.start()
    start = time.time()
    pool_hendler()
    print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
    print("All done! {}".format(time.time() - start))

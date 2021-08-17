import time
import tracemalloc
from multiprocessing import Pool

def single_function(x):
    return x ** x

def main():
    p = Pool()
    p.map(single_function, [i for i in range(1000000, 1000016)])

if __name__ == "__main__":
    tracemalloc.start()
    start = time.time()
    
    main()

    print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
    print("All done! {}".format(time.time() - start))

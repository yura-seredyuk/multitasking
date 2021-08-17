import time
import tracemalloc
import threading

def single_function(x):
    return x ** x

threads = []
tracemalloc.start()
start = time.time()
for i in range(1000000, 1000016):
    thread = threading.Thread(target=single_function, args = (i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
print("All done! {}".format(time.time() - start))

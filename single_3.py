import time
import tracemalloc

def single_function(x):
    return x ** x

tracemalloc.start()
start = time.time()
for i in range(1000000, 1000016):
    single_function(i)

print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
print("All done! {}".format(time.time() - start))

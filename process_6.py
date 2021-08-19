import time
import tracemalloc
import requests
from multiprocessing import Pool


def clear_file():
    with open('to_do_file.txt', 'w') as f:
        f.close()

def single_function(id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos/{id}')
    data = response.json()

    with open('to_do_file.txt', 'a') as f:
        f.write(f'id:{data["id"]} userId:{data["userId"]} title:{data["title"]} completed:{data["completed"]}\n')

def pool_handler():
    p = Pool()
    p.map(single_function, [i for i in range(1,201)])

if __name__ == '__main__':
    clear_file()
    tracemalloc.start()
    start = time.time()
    
    pool_handler()

    print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
    print("All done! {}".format(time.time() - start))

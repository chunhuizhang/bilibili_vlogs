import os
from multiprocessing import Process, Pool, Manager
from random import random
from threading import Thread
import os



def monte_carlo_pi(i, n=5000_0000):
    print('epoch: {}'.format(i))
    cnt = 0
    for i in range(n):
        x, y = random(), random()
        if x**2 + y**2 <= 1:
            cnt += 1
    return 4*cnt/n


if __name__ == '__main__':
    # pool = Pool(os.cpu_count()//2)
    # pool.map(monte_carlo_pi, range(10))

    thread_list = []
    n_threads = 10
    for i in range(n_threads):
        t = Thread(target=monte_carlo_pi, args=(i, ))
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()

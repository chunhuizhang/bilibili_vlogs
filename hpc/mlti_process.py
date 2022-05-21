import os
from multiprocessing import Process, Pool, Manager
from random import random


def monte_carlo_pi(i, n=5000_0000):
    print('epoch: {}'.format(i))
    cnt = 0
    for i in range(n):
        x, y = random(), random()
        if x**2 + y**2 <= 1:
            cnt += 1
    return 4*cnt/n


if __name__ == '__main__':
    pool = Pool(os.cpu_count()//2)
    pool.map(monte_carlo_pi, range(10))

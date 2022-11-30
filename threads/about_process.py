
from multiprocessing import Process
import os
import time


def run():
    while True:
        print(f'current process id: {os.getpid()}')
        print(f'parent process id of current process {os.getpid()}: {os.getppid()}')
        time.sleep(2)


def run2():
    while True:
        print(f'current process id: {os.getpid()}')
        print(f'parent process id of current process {os.getpid()}: {os.getppid()}')
        time.sleep(2)


if __name__ == '__main__':
    p1 = Process(target=run)
    p1.start()
    p2 = Process(target=run2)
    p2.start()

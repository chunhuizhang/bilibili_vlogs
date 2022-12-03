

from threading import Thread
from queue import Queue
import random
import time


BUF_SIZE = 10

q = Queue(BUF_SIZE)


class ProducerThread(Thread):
    def __init__(self, name=None):
        super(ProducerThread, self).__init__()
        self.name = name

    def run(self):
        while True:
            if not q.full():
                item = random.randint(1, 10)
                q.put(item)
                print(f'{self.name}({self.ident}): puts {item}, current queue size is {q.qsize()}')
                time.sleep(random.random())
            else:
                print(f'{self.name}({self.ident}): is full, cannot produce.')
                time.sleep(random.random()*2)


class ConsumerThread(Thread):
    def __init__(self, name=None):
        super(ConsumerThread, self).__init__()
        self.name = name

    def run(self):
        while True:
            if not q.empty():
                item = q.get()
                print(f'{self.name}({self.ident}): gets {item}, current queue size is {q.qsize()}')
                time.sleep(random.random())
            else:
                print(f'{self.name}({self.ident}): is empty, cannot consume, waiting.')
                time.sleep(random.random()*2)


if __name__ == '__main__':
    p1 = ProducerThread(name='producer-1')
    p1.start()
    time.sleep(2)

    c1 = ConsumerThread(name='consumer-1')
    c1.start()


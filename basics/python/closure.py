
from random import randint

def outer(msg):
    value = randint(0, 100)
    message = msg
    def inner():
        print(msg)
    return inner

if __name__ == '__main__':
    f = outer('zhang')
    f()
    f()
    f()


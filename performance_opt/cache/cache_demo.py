
from functools import lru_cache
import functools


@lru_cache(256)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)




if __name__ == '__main__':
    print(functools._make_key((4, 6), {}, False))
    print(fib(5))
    print(fib.cache_info())

    d = {object()}
    

import matplotlib.pyplot as plt
import math


def fn(n):
    return (1+1/n)**n



if __name__ == '__main__':

    plt.plot(range(1, 500), list(map(fn, range(1, 500))), marker='.')
    plt.hlines(y=math.e, xmin=0, xmax=500, ls='dashed', color='gray')
    plt.show()

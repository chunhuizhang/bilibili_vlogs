import numpy as np


def gini(x):
    mean = np.mean(x)
    mad = np.mean(np.abs(x - mean))
    rmad = mad/mean
    return rmad/2


if __name__ == '__main__':

    x = np.asarray([2, 2, 4, 4])
    print(gini(x))
    x = np.asarray([1, 1, 6, 4])
    print(gini(x))

    x = np.random.rand(500)
    print(gini(x))
    x = np.random.rand(500)+1
    print(gini(x))
    x = np.random.rand(500)+10
    print(gini(x))
    x = np.random.rand(500)+100
    print(gini(x))



import random
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd


def random_walk(N):
    x = 0
    for i in range(N):
        dx = random.choice([1, -1])
        x += dx
    return x


if __name__ == '__main__':
    n_samples = 50000
    final_x = []
    for i in range(n_samples):
        final_x.append(random_walk(100))
    pd.Series(final_x).value_counts().sort_index().plot(kind='bar')
    plt.show()

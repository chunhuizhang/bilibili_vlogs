
import numpy as np
import matplotlib.pyplot as plt

years = [y+2009 for y in range(11)]
gmvs = [0.5, 9.36, 52, 191, 350, 571, 912, 1207, 1682, 2135, 2684]


def polynomial(xs, ys, n):
    f = np.polyfit(xs, ys, n)
    def func(x):
        return sum(f[i]*x**(n-i)for i in range(n+1))
    return func

f = polynomial(years, gmvs, 3)
print(f(2020))

plt.plot(years, gmvs, marker='o')
plt.show()
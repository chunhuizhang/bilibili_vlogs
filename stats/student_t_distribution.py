
from scipy.special import gamma
import math
import matplotlib.pyplot as plt
import numpy as np


def t_dist(t, v):
    return gamma((v+1)/2)/(math.sqrt(v*math.pi)*gamma(v/2)) * (1+t**2/v)**(-(v+1)/2)


x = np.arange(-4, 4, .1)
plt.plot(x, t_dist(x, 1), label='v=1')
plt.plot(x, t_dist(x, 2), label='v=2')
plt.plot(x, t_dist(x, 5), label='v=5')
# plt.plot(x, t_dist(x, math.inf), label='v=inf')
plt.legend()
plt.show()


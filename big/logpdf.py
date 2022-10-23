
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, poisson


# fig, axes = plt.subplots(1, 2)
# x = list(range(10))
# axes[0].plot(x, norm.logpdf(x, loc=5, scale=2), 'r-', lw=2, alpha=0.6, label='norm logpdf')
# axes[0].legend()
# axes[1].plot(x, poisson.logpmf(x, mu=0.6), 'b-', lw=2, alpha=0.6, label='poisson logpmf')
# axes[1].legend()
# # plt.legend()
# plt.show()

fig, axes = plt.subplots(1, 2)
x = list(range(10))
axes[0].plot(x, norm.pdf(x, loc=5, scale=2), 'r-', lw=2, alpha=0.6, label='norm pdf')
axes[0].legend()
axes[1].plot(x, poisson.pmf(x, mu=0.6), 'b-', lw=2, alpha=0.6, label='poisson pmf')
axes[1].legend()
# plt.legend()
plt.show()
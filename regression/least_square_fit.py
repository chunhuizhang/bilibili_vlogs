import numpy as np
from numpy.linalg import inv

x = np.array([1, 2, 3, 4, 5]).reshape((-1, 1))
y = np.array([2, 4, 5, 4, 5]).reshape((-1, 1))


x_aug = np.hstack([np.ones_like(x), x])

# (X^TX)^(-1)*X^T*y
# y = 2.2 + 0.6*x
beta = inv(x_aug.transpose().dot(x_aug)).dot(x_aug.transpose()).dot(y)

print(beta)

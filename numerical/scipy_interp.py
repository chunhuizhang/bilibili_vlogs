import numpy as np

from scipy import interpolate
x = np.asarray(range(2))
y = np.asarray(range(2))
z = np.asarray([[10, 40], [30, 20]])
f = interpolate.interp2d(x, y, z, kind='linear')

for x in range(6):
    for y in range(6):
        print(x, y, f(x, y))

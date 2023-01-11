import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm

landscape = np.random.randint(1, high=50, size=(10, 10))

xs, ys = np.meshgrid(range(10), range(10))

# zs = landscape[xs, ys]
zs = (xs-4)**2 + (ys-3)**2
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(xs, ys, zs, rstride=1, cstride=1, cmap=cm.jet, linewidth=0)
fig.colorbar(surf)

title = ax.set_title("plot_surface: given X, Y and Z as 2D:")
title.set_y(np.max(zs)+0.01)

# ax.xaxis.set_major_locator(MaxNLocator(5))
# ax.yaxis.set_major_locator(MaxNLocator(6))
# ax.zaxis.set_major_locator(MaxNLocator(5))

fig.tight_layout()

plt.show()

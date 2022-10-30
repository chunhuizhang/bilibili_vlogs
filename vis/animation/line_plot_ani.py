import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'ro')

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)


def init():
    # print('init')
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,


def animate(i):
    # print('animate', i)
    xdata.append(i)
    ydata.append(np.sin(i))
    ln.set_data(xdata, ydata)
    return ln,


ani = FuncAnimation(fig,
                    animate,
                    frames=np.linspace(0, 2*np.pi, 128),
                    # init_func=init,
                    blit=True
                    )
plt.show()


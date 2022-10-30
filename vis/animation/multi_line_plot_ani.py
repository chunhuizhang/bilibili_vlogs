import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, axes = plt.subplots(1, 2)

xdata, ydata1, ydata2 = [], [], []

ln1, = axes[0].plot([], [], 'ro')
ln2, = axes[1].plot([], [], 'go')


def init():
    # print('init')
    axes[0].set_xlim(0, 2*np.pi)
    axes[0].set_ylim(-1, 1)
    axes[1].set_xlim(0, 2*np.pi)
    axes[1].set_ylim(-1, 1)
    return ln1, ln2,


def animate(i):
    # print('animate', i)
    xdata.append(i)
    ydata1.append(np.sin(i))
    ln1.set_data(xdata, ydata1)

    ydata2.append(np.cos(i))
    ln2.set_data(xdata, ydata2)
    return ln1, ln2,


ani = FuncAnimation(fig,
                    animate,
                    frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init,
                    blit=True
                    )
plt.show()


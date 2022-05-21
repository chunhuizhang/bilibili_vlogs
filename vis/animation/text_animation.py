from matplotlib import pyplot as plt, animation

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots()
ax.set(xlim=(-1, 1), ylim=(-1, 1))
string = 'Hello, how are you doing?'
label = ax.text(0, 0, string[0], ha='center', va='center', fontsize=20, color="Red")


def animate(i):
    label.set_text(string[:i + 1])


anim = animation.FuncAnimation(
    fig, animate, interval=100, frames=len(string))
ax.axis('off')
plt.show()


import gym
import time
import matplotlib.pyplot as plt
from matplotlib import animation


env_name = 'CartPole-v0'

env = gym.make(env_name)

state = env.reset()
done = False
total_score = 0
frames = []
while not done:
    frames.append(env.render(mode='rgb_array'))
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    total_score += reward
    time.sleep(0.1)


def display_frame_as_gif(frames):
    plt.figure(figsize=(frames[0].shape[1]/72, frames[0].shape[0]/72), dpi=72)
    patch = plt.imshow(frames[0])
    plt.axis('off')

    def animate(i):
        patch.set_data(frames[i])

    anim = animation.FuncAnimation(plt.gcf(), animate, frames=len(frames), interval=50)
    anim.save('movie_cartpole.gif')


env.close()

print(len(frames), frames[0].shape)
# display_frame_as_gif(frames)


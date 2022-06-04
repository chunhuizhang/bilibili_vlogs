
import gym
# 创建一个小车倒立摆模型
env = gym.make('CartPole-v0')
# 初始化环境
env.reset()
# 刷新当前环境，并显示
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # take a random action
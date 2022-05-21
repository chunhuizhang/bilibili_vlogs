
import gym
import numpy as np

class BespokeAgent:
    def __init__(self, env):
        pass

    def decide(self, observation):
        position, velocity = observation
        lb = min(-0.09*(position + 0.25) ** 2 + 0.03, 0.3*(position + 0.9)**4 - 0.008)
        ub = -0.07*(position + 0.38) ** 2 + 0.07
        if lb < velocity < ub:
            action = 2
        else:
            action = 0
        # print('observation: {}, lb: {}, ub: {} => action: {}'.format(observation, lb, ub, action))
        return action

    def learn(self, *argg):
        pass


def play(i, agent, env, render=True, train=False):
    episode_reward = 0
    observation = env.reset()
    while True:
        if render:
            env.render()
        action = agent.decide(observation)
        next_observation, reward, done, _ = env.step(action)
        episode_reward += reward
        if train:
            agent.learn(observation, action, reward, done)
        if done:
            env.close()
            break
        observation = next_observation
    print(i, episode_reward)
    return i, episode_reward


if __name__ == '__main__':
    env = gym.make('MountainCar-v0')
    agent = BespokeAgent(env)
    rewards = [play(i, agent, env) for i in range(100)]
    print(rewards)

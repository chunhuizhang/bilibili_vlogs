
import gym
import numpy as np

env_name = 'CartPole-v1'

env = gym.make(env_name)


class Agent:
    def __init__(self, env):
        self.action_size = env.action_space.n

    def action_policy(self, observation):
        pos, vel, angle, _ = observation
        if angle < 0:
            return 0
        return 1


if __name__ == '__main__':

    observation = env.reset()
    agent = Agent(env)
    reward_history = []
    for _ in range(100):
        # env.render()
        # action = agent.action_policy(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        reward_history.append(reward)
        if done:
            # env.env.close()
            env.reset()
    print(reward_history, np.mean(reward_history))

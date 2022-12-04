

import gym
import time
from datetime import datetime
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy


env_name = 'CartPole-v1'
env = gym.make(env_name)

episodes = 5
for episode in range(1, episodes + 1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action)
        print(reward, done)
        score += reward
        # time.sleep(0.5)
    now = datetime.now().strftime('%H:%M:%S')
    print('{}, Episode:{} Score:{}'.format(now, episode, score))
env.close()

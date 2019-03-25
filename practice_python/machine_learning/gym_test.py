#! /usr/bin/env python3
# -*- coding = utf-8 -*-

""" this is origin codes by OpenAI manuals
import gym
env = gym.make('CartPole-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
"""

import gym
env = gym.make('CartPole-v0')
iter_num = 50;
for i_episode in range(iter_num):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            print((i_episode+1), "/", iter_num)
            break
env.close()

# -*- coding:utf-8 -*-

'''
Sample script for gym renju.
@auther: Arata Kokubun
@date: 2017/12/23
'''

# Imports
import gym
import time
# Change import on installed on pip
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import gym_renju
env = gym.make('Renju19x19-v0') # default 'beginner' level opponent policy

env.reset()
env.render()
# env.step(15) # place a single stone, black color first

# play a game
env.reset()
for _ in range(225):
    action = env.action_space.sample() # sample without replacement
    observation, reward, done, info = env.step(action)
    print(reward)
    env.render()
    time.sleep(0.05)
    if done:
        print ("Game is Over")
        break

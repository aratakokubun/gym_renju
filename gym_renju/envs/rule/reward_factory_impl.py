# -*- coding:utf-8 -*-

'''
Implemented factory module for reward.
@auther: Arata Kokubun
@date: 2017/12/23
'''

# Imports
import os

from gym_renju.envs.core.contract.reward import Reward
from gym_renju.envs.core.contract.factory import RewardFactory
from gym_renju.envs.rule.renju_reward import ConfiguredReward

class RewardFactoryImpl(RewardFactory):
  def generate(self) -> Reward:
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../../data/reward.json")
    return ConfiguredReward(path)

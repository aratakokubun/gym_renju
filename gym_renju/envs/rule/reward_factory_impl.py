# -*- coding:utf-8 -*-

'''
Implemented factory module for reward.
@auther: Arata Kokubun
@date: 2017/12/23
'''

# Imports
from gym_renju.envs.core.contract.reward import Reward
from gym_renju.envs.core.contract.factory import RewardFactory
from gym_renju.envs.rule.renju_reward import ConfiguredReward

class RewardFactoryImpl(RewardFactory):
  def generate(self) -> Reward:
    return ConfiguredReward('gym_renju/data/reward.json')

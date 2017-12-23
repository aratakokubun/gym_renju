# -*- coding:utf-8 -*-

'''
Reward interface module for renju.
@auther: Arata Kokubun
@date: 2017/12/23
'''

# Imports
from gym_renju.envs.core.domain.player import PlayerColor
from gym_renju.envs.core.domain.result import Result

class Reward(object):
  def get_reward(self, player: PlayerColor, result: Result) -> float:
    '''
    Get reward for the specified result
    '''
    raise NotImplementedError

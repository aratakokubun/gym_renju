# -*- coding:utf-8 -*-

'''
AI player for Renju.
@auther: Arata Kokubun
@data: 2017/12/23
'''

# Imports
from typing import List

from gym_renju.envs.core.domain.player import PlayerColor
from gym_renju.envs.core.contract.policy import PlayerPolicy
from gym_renju.envs.core.contract.space import DiscreteSpace

class AiPolicy(PlayerPolicy):
  '''
  Policy for AI player
  '''
  def auto_act(self) -> bool:
    return False

class RandomPolicy(AiPolicy):
  '''
  Policy for random AI player
  '''
  def act(self, state: List[int], action_space: DiscreteSpace, color: PlayerColor) -> int:
    return action_space.sample()

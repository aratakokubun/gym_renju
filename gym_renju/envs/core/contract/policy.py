# -*- coding:utf-8 -*-

'''
Player interface module for Renju.
@auther: Arata Kokubun
@data: 2017/12/21
'''

# Imports
from typing import List

from gym_renju.envs.core.domain.player import PlayerColor
from gym_renju.envs.core.contract.space import DiscreteSpace

class PlayerPolicy(object):
  '''
  Interface for renju player
  '''
  def act(self, state: List[int], action_space: DiscreteSpace, color: PlayerColor) -> int:
    raise NotImplementedError

  def auto_act(self) -> bool:
    raise NotImplementedError

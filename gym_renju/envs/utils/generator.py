# -*- coding:utf-8 -*-

'''
Utility module for generating game states.
@auther: Arata Kokubun
@data: 2017/12/09
'''

# Imports
from typing import List
from gym_renju.envs.player import PlayerColor
import random

class BoardStateGenerator(object):
  @staticmethod
  def generate_empty(board_size: int) -> List[int]:
    return [PlayerColor.EMPTY for _ in range(board_size**2)]

  @staticmethod
  def generate_random(board_size: int) -> List[int]:
    return [random.choice(list(PlayerColor)) for _ in range(board_size**2)]
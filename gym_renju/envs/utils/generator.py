# -*- coding:utf-8 -*-

'''
Utility module for generating game states and matchers.
@auther: Arata Kokubun
@data: 2017/12/09
'''

# Imports
import random
from typing import List

from gym_renju.envs.core.domain.player import PlayerColor
from gym_renju.envs.utils import utils

class BoardStateGenerator(object):
  @staticmethod
  def generate_empty(board_size: int) -> List[int]:
    return [PlayerColor.EMPTY.value for _ in range(board_size**2)]

  @staticmethod
  def generate_random(board_size: int) -> List[int]:
    return [random.choice(list(PlayerColor)).value for _ in range(board_size**2)]

  @staticmethod
  def generate_full(board_size: int) -> List[int]:
    return [random.choice(utils.valid_player_colors()).value for _ in range(board_size**2)]

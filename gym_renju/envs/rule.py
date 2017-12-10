# -*- coding:utf-8 -*-

'''
Rule definition modules for Renju Game .
@auther: Arata Kokubun
@data: 2017/12/04
'''

import gym_gomoku
import numpy as np
import gym
from gym import spaces
from gym import error
from gym.utils import seeding
from six import StringIO
import sys
import six
from typing import List, Tuple, Dict
import operator

from gym_renju.envs.renju import RenjuBoard
from gym_renju.envs.player import PlayerColor, PlayerLatest
from gym_renju.envs.utils import utils
from gym_renju.envs.utils import rule_pattern_compile as rpc

def search_sequence(board_state: List[int], start: int, search_dir: Tuple, size: int) -> List:
  '''
  Search sequencial color in the board.
  @param board_state: board to search from
  @param start: search start index
  @param search_dir: search direction
  @param size: board size
  @return pair of (number of sequence, color)
  '''
  color = board_state[start]
  to_next = lambda c: tuple(map(operator.add, c, search_dir))
  in_range = lambda c: 0 <= c[0] < size and 0 <= c[1] < size
  next_coords = to_next(utils.index_to_coords(start, size))
  count = 1
  while in_range(next_coords):
    if color is board_state[utils.coords_to_index(next_coords, size)]:
      count += 1
      next_coords = to_next(next_coords)
    else:
      break
  return (count, color)


def win_game(board_state: List[int], current_player: PlayerColor, patterns: Dict) -> bool:
  pass

def lose_game(board_state: List[int], current_player: PlayerColor, patterns: Dict, latest_action: int) -> bool:
  pass

def judge_game(board_state: List[int], current_player: PlayerColor, latest_action: int) -> any:
  patterns = rpc.pcompile(current_player, latest_action)
  is_win = win_game(board_state, current_player, patterns)

def legal_actions(board_state: List[int]) -> List[int]:
  '''
  Return list of legal actions based on the board state and current player color.
  Contains actions resulted in lose because of against of the rule.
  '''
  legal = lambda s: s[1] is PlayerColor.EMPTY
  action = lambda s: s[0]
  return list(map(action, filter(legal, enumerate(board_state))))

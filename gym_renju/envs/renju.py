# -*- coding:utf-8 -*-

'''
Renju Game Model Modules.
@auther: Arata Kokubun
@data: 2017/12/04
'''

import numpy as np
import gym
from gym import spaces
from gym import error
from gym.utils import seeding
from six import StringIO
import sys
import six
from typing import List
import copy

from gym_renju.envs.player import PlayerColor, PlayerType
from gym_renju.envs import rule
from gym_renju.envs.utils import utils
from gym_renju.envs.utils.generator import BoardStateGenerator as bsg

class RenjuState(object):
  '''
  Renju State class to preserve a current player and a board.
  '''
  def __init__(self, board: List, player_color: PlayerColor) -> None:
    assert player_color in utils.valid_player_colors()
    self._board = board
    self._player_color = player_color

  def act(self, action):
    return RenjuState(self._board.play(action, self._player_color),
      utils.next_player(self._player_color))

  def __repr__(self):
    '''
    Output board state
    '''
    return 'To play: {}\n{}'.format(six.u(self._player_color), self._board.__repr__())

class RenjuBoard(object):
  '''
  Implementation of renju board.
  '''

  def __init__(self, board_size):
    self._board_size = board_size
    self._board_state = bsg.generate_empty(board_size)
    self._move_count = 0
    self._last_action = None

  def act(self, action: int, player_color: PlayerColor) -> any:
    assert action in rule.legal_actions(self._board_state)
    next_board = RenjuBoard(self._board_size)
    next_board.copy_state(self)
    next_board.receive_act(action, player_color)
    return next_board

  def receive_act(self, action: int, player_color: PlayerColor) -> None:
    self._board_state[action] = player_color
    self._move_count += 1
    self._last_action = action

  def get_board_size(self) -> int:
    return self._board_size

  def get_board_state(self) -> List[int]:
    return self._board_state

  def set_board_state(self, board_state: List[int]) -> None:
    self._board_state = board_state

  def copy_state(self, board: any) -> None:
    self.set_board_state(copy.deepcopy(board._board_state))
    self._move_count = board._move_count

  def to_np_arr(self) -> np.array:
    return np.array(self._board_state)

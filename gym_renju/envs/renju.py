# -*- coding:utf-8 -*-

'''
Renju Game Model Modules.
@auther: Arata Kokubun
@data: 2017/12/04
'''

# Imports
from typing import List

import copy
import numpy as np
import six

from gym_renju.envs.core.domain.player import PlayerColor
from gym_renju.envs.rule import rule
from gym_renju.envs.utils import utils
from gym_renju.envs.utils.generator import BoardStateGenerator as bsg

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
    self._board_state[action] = player_color.value
    self._move_count += 1
    self._last_action = action

  def get_board_size(self) -> int:
    return self._board_size

  def get_board_state(self) -> List[int]:
    return self._board_state

  def set_board_state(self, board_state: List[int]) -> None:
    self._board_state = board_state

  def copy_state(self, board: any) -> None:
    self.set_board_state(copy.deepcopy(board.get_board_state()))
    self._move_count = board.get_move_count()

  def to_np_arr(self) -> np.array:
    return np.array(self._board_state)

  def get_move_count(self) -> int:
    return self._move_count

  def get_last_action(self) -> int:
    return self._last_action

  def __repr__(self):
    out = ""

    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:self._board_size]
    label_move = "Move: " + str(self._move_count) + "\n"
    label_letters = "     " + " ".join(letters) + "\n"
    label_boundry = "   " + "+-" + "".join(["-"] * (2 * self._board_size)) + "+" + "\n"

    # construct the board output
    out += (label_move + label_letters + label_boundry)

    for i in range(self._board_size - 1, -1, -1):
        line = ""
        line += (str("%2d" % (i + 1)) + " |" + " ")
        for j in range(self._board_size):
            # check if it's the last move
            index = i * self._board_size + j
            line += utils.color_to_symbol(self._board_state[index])
            if self._last_action and index == self._last_action:
                line += ")"
            else:
                line += " "
        line += ("|" + "\n")
        out += line
    out += (label_boundry + label_letters)
    return out

  def __eq__(self, other):
    if isinstance(self, other.__class__):
        return self._board_size == other._board_size and self._board_state == other._board_state and \
          self._move_count == other._move_count and self._last_action == other._last_action
    return False

class RenjuState(object):
  '''
  Renju State class to preserve a current player and a board.
  '''
  def __init__(self, board: RenjuBoard, latest_player: PlayerColor, next_player: PlayerColor) -> None:
    assert next_player in utils.valid_player_colors()
    self._board = board
    self._latest_player = latest_player
    self._next_player = next_player

  def act(self, action: int):
    return RenjuState(self._board.act(action, self._next_player),
      self._next_player, utils.next_player(self._next_player))

  def get_board(self) -> RenjuBoard:
    return self._board

  def get_latest_player(self) -> PlayerColor:
    return self._latest_player

  def get_next_player(self) -> PlayerColor:
    return self._next_player

  def __repr__(self):
    '''
    Output board state
    '''
    return 'To play: {}\n{}'.format(six.u(self._next_player), self._board.__repr__())

  def __eq__(self, other):
    if isinstance(self, other.__class__):
        return self._board == other._board and \
          self._latest_player == other._latest_player and \
          self._next_player == other._next_player
    return False

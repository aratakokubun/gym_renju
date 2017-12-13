# -*- coding:utf-8 -*-

'''
Integration Test module for rule.
@auther: Arata Kokubun
@data: 2017/12/14
'''

# Imports
import unittest as ut
from typing import Tuple, List
from parameterized import parameterized
from gym_renju.envs.player import PlayerColor
from gym_renju.envs import rule
from gym_renju.envs.utils.generator import BoardStateGenerator as bsg

# Shorten constants
BLACK = PlayerColor.BLACK
WHITE = PlayerColor.WHITE
EMPTY = PlayerColor.EMPTY

class WinIntegrationTest(ut.TestCase):
  def setUp(self):
    self.board_state = [
        1, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 0, 0, 1,
        0, 0, 0, 1, 0, 1, 0, 0, 1,
        0, 0, 0, 0, 1, 0, 0, 0, 1,
        0, 0, 0, 1, 0, 0, 0, 1, 1,
        0, 0, 1, 0, 0, 0, 1, 0, 1,
        0, 0, 1, 1, 2, 1, 1, 1, 0,
        0, 0, 0, 0, 1, 0, 0, 0, 0
    ]
    self.board_size = 9

  @parameterized.expand([
    [0, True],
    [20, True],
    [21, True],
    [62, True],
    [68, True],
    [1, False],
    [32, False],
    [65, False],
  ])
  def test_is_win_game(self, latest_action: int, is_win: bool):
    actual = rule.win_game(self.board_state, self.board_size, PlayerColor.BLACK, latest_action)
    self.assertEqual(is_win, actual)

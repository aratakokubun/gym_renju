# -*- coding:utf-8 -*-

'''
Test module for renju.
@auther: Arata Kokubun
@date: 2018/1/3
'''

# Imports
import unittest as ut
from unittest.mock import MagicMock
from parameterized import parameterized

from gym_renju.envs.core.domain.player import PlayerColor
from gym_renju.envs.renju import RenjuBoard, RenjuState
from gym_renju.envs.utils.generator import BoardStateGenerator as bsg

class RenjuBoardTest(ut.TestCase):
  def test_act(self):
    board_size = 15
    action = 1
    before_board = RenjuBoard(board_size)
    actual_board = before_board.act(action, PlayerColor.WHITE)
    expected_board_state = bsg.generate_empty(board_size)
    expected_board_state[action] = 2
    self.assertEqual(15, actual_board.get_board_size())
    self.assertEqual(expected_board_state, actual_board.get_board_state())
    self.assertEqual(1, actual_board.get_move_count())
    self.assertEqual(1, actual_board.get_last_action())

class RenjuStateTest(ut.TestCase):
  def test_act(self):
    before_board = RenjuBoard(15)
    expected_board = RenjuBoard(9) 
    before_board.act = MagicMock()
    before_board.act.return_value = expected_board
    before_state = RenjuState(before_board, None, PlayerColor.BLACK)
    actual_state = before_state.act(19)
    self.assertEqual(expected_board, actual_state.get_board())
    self.assertEqual(PlayerColor.BLACK, actual_state.get_latest_player())
    self.assertEqual(PlayerColor.WHITE, actual_state.get_next_player())
    before_board.act.assert_called_with(19, PlayerColor.BLACK)

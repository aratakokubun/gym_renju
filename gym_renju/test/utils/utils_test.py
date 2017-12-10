# -*- coding:utf-8 -*-

'''
Test module for renju utils.
@auther: Arata Kokubun
@data: 2017/12/09
'''

# Imports
import unittest as ut
from gym_renju.envs.utils import utils
from gym_renju.envs.player import PlayerColor, PlayerType, PlayerLatest
from gym_renju.envs.utils.generator import BoardStateGenerator as bsg

class UtilsTest(ut.TestCase):
  def test_next_player_white_is_black(self):
    current = PlayerColor.WHITE
    expected = PlayerColor.BLACK
    self.assertEqual(expected, utils.next_player(current))

  def test_next_player_black_is_white(self):
    current = PlayerColor.BLACK
    expected = PlayerColor.WHITE
    self.assertEqual(expected, utils.next_player(current))

  def test_index_to_coords(self):
    index = 100
    board_size = 12
    expected = (8, 4)
    self.assertEqual(expected, utils.index_to_coords(index, board_size))

  def test_coords_to_index(self):
    coords = (7, 5)
    board_size = 9
    expected = 68
    self.assertEqual(expected, utils.coords_to_index(coords, board_size))

  def test_get_target_lines(self):
    size = 15
    latest_action = 50
    board = [i for i in range(size**2)]
    expected_line_row = [i for i in range(45, 60)]
    expected_line_col = [i for i in range(5, 15**2, 15)]
    expected_line_rb = [i for i in range(2, 15**2, 16)]
    expected_line_lb = [i for i in range(8, 15**2, 14)]
    actual_lines = utils.get_target_lines(board, size, latest_action)
    self.assertEqual(expected_line_row, actual_lines[0])
    self.assertEqual(expected_line_col, actual_lines[1])
    self.assertEqual(expected_line_rb, actual_lines[2])
    self.assertEqual(expected_line_lb, actual_lines[3])

  def test_mark_latest(self):
    size = 15
    latest_action = 60
    board = bsg.generate_empty(15)
    board[latest_action] = PlayerColor.BLACK
    copied_board = utils.mark_latest(board, size, latest_action)
    self.assertEqual(PlayerLatest.BLACK, copied_board[latest_action])

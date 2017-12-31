# -*- coding:utf-8 -*-

'''
Test module for renju rule.
@auther: Arata Kokubun
@data: 2017/12/09
'''

# Imports
import unittest as ut
from typing import Tuple, List
from parameterized import parameterized

from gym_renju.envs.core.domain.player import PlayerColor
from gym_renju.envs.rule import rule
from gym_renju.envs.utils.generator import BoardStateGenerator as bsg

# Shorten constants
BLACK = PlayerColor.BLACK.value
WHITE = PlayerColor.WHITE.value
EMPTY = PlayerColor.EMPTY.value

class RuleTest(ut.TestCase):
  @parameterized.expand([[7], [9], [15], [19]])
  def test_legal_actions(self, input_size: int):
    board_state = bsg.generate_random(input_size)
    actual_actions = rule.legal_actions(board_state)
    for index, state in enumerate(board_state):
      if index in actual_actions:
        self.assertEqual(EMPTY, state)
      else:
        self.assertNotEqual(EMPTY, state)

  @parameterized.expand([
    # [size, dir, start, [colors], expected(count, color)]
    [7, (1, 0), 2, [BLACK, BLACK, WHITE, BLACK], (2, BLACK)],
    [7, (1, 0), 10, [EMPTY, EMPTY, EMPTY, BLACK], (3, EMPTY)],
    [9, (0, 1), 9, [WHITE, WHITE, WHITE, EMPTY, BLACK, WHITE], (3, WHITE)],
    [15, (1, 1), 35, [BLACK, WHITE, WHITE, EMPTY], (1, BLACK)],
    [19, (1, -1), 3, [WHITE, WHITE, WHITE, WHITE], (4, WHITE)]])
  def test_search_sequence(self, size: int, direc: Tuple, start: int,
    colors: List, expected: Tuple):
    board_state = bsg.generate_empty(size)
    index = start
    for color in colors:
      board_state[index] = color
      index = index + direc[0] * size + direc[1]
    actual = rule.search_sequence(board_state, start, direc, size)
    self.assertEqual(actual, expected)

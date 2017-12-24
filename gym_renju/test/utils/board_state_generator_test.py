# -*- coding:utf-8 -*-

'''
Test module for BoardStateGenerator.
@auther: Arata Kokubun
@data: 2017/12/09
'''

# Imports
import unittest as ut
from parameterized import parameterized

from gym_renju.envs.core.domain.player import PlayerColor
from gym_renju.envs.utils.generator import BoardStateGenerator as bsg

class BoardStateGeneratorTest(ut.TestCase):
  @parameterized.expand([[7], [9], [15], [19]])
  def test_generate_all_empty_as_size(self, size_input: int):
    actual = bsg.generate_empty(size_input)
    self.assertEqual(size_input**2, len(actual))
    self.assertTrue(all([s is PlayerColor.EMPTY.value for s in actual]))

  @parameterized.expand([[7], [9], [15], [19]])
  def test_generate_full_as_size(self, size_input: int):
    actual = bsg.generate_full(size_input)
    self.assertEqual(size_input**2, len(actual))
    self.assertTrue(all([s in [PlayerColor.BLACK.value, PlayerColor.WHITE.value] for s in actual]))

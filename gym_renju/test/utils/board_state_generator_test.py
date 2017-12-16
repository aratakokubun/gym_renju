# -*- coding:utf-8 -*-

'''
Test module for BoardStateGenerator.
@auther: Arata Kokubun
@data: 2017/12/09
'''

# Imports
import unittest as ut
import pytest
from parameterized import parameterized
from gym_renju.envs.utils.generator import BoardStateGenerator as bsg
from gym_renju.envs.domain.player import PlayerColor

# @pytest.mark.parametrize('size_input', [9,19,7])
class BoardStateGenerator(ut.TestCase):
  @parameterized.expand([[7], [9], [15], [19]])
  def test_generate_all_empty_as_size(self, size_input: int):
    actual = bsg.generate_empty(size_input)
    self.assertEqual(size_input**2, len(actual))
    self.assertTrue(all([s is PlayerColor.EMPTY for s in actual]))

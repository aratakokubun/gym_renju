# -*- coding:utf-8 -*-

'''
Test module for PolicyGenerator.
@auther: Arata Kokubun
@data: 2017/12/23
'''

# Imports
import unittest as ut
from parameterized import parameterized

from gym_renju.envs.core.domain.player import PlayerColor
from gym_renju.envs.policy.ai import RandomPolicy
from gym_renju.envs.policy.input import InputPolicy
from gym_renju.envs.utils.generator import PolicyGenerator

class BoardStateGenerator(ut.TestCase):
  @parameterized.expand([['input', InputPolicy], ['random', RandomPolicy]])
  def test_generate_all_empty_as_size(self, policy: str, clazz: type):
    actual = PolicyGenerator.generate(policy)
    self.assertEqual(clazz, type(actual))

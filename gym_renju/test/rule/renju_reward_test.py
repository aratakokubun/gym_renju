# -*- coding:utf-8 -*-

'''
Test module for renju policy.
@auther: Arata Kokubun
@date: 2017/12/23
'''

# Imports
import unittest as ut
from parameterized import parameterized

from gym_renju.envs.core.domain.player import PlayerColor
from gym_renju.envs.core.domain.result import Result
from gym_renju.envs.rule.renju_reward import ConfiguredReward

class RenjuRewardNoConfigTest(ut.TestCase):
  def setUp(self):
    self.reward = ConfiguredReward()

  @parameterized.expand([
    [PlayerColor.BLACK, Result.WIN, 1.0],
    [PlayerColor.BLACK, Result.LOSE, -1.0],
    [PlayerColor.BLACK, Result.DRAW, 0.0],
    [PlayerColor.BLACK, Result.NONE, 0.0],
    [PlayerColor.WHITE, Result.WIN, 1.0],
    [PlayerColor.WHITE, Result.LOSE, -1.0],
    [PlayerColor.WHITE, Result.DRAW, 0.0],
    [PlayerColor.WHITE, Result.NONE, 0.0],
  ])
  def test_get_valid_reward(self, player: PlayerColor, result: Result, expected_reward: float):
    actual_reward = self.reward.get_reward(player, result)
    self.assertEqual(expected_reward, actual_reward)

class RenjuRewardSpecifiedConfigTest(ut.TestCase):
  def setUp(self):
    self.reward = ConfiguredReward('gym_renju/data/test_reward.json')

  @parameterized.expand([
    [PlayerColor.BLACK, Result.WIN, 1.5],
    [PlayerColor.BLACK, Result.LOSE, -0.5],
    [PlayerColor.BLACK, Result.DRAW, -2.5],
    [PlayerColor.BLACK, Result.NONE, 4.0],
    [PlayerColor.WHITE, Result.WIN, 1.5],
    [PlayerColor.WHITE, Result.LOSE, -0.5],
    [PlayerColor.WHITE, Result.DRAW, 3.0],
    [PlayerColor.WHITE, Result.NONE, 4.0],
  ])
  def test_get_valid_reward(self, player: PlayerColor, result: Result, expected_reward: float):
    actual_reward = self.reward.get_reward(player, result)
    self.assertEqual(expected_reward, actual_reward)

# -*- coding:utf-8 -*-

'''
Test module for renju env.
@auther: Arata Kokubun
@date: 2018/1/3
'''

# Imports
import unittest as ut
from unittest.mock import MagicMock, patch
from parameterized import parameterized
import numpy as np
from gym import error

from gym_renju.envs.core.domain.player import PlayerColor
from gym_renju.envs.core.domain.result import Result
from gym_renju.envs.renju import RenjuBoard, RenjuState
from gym_renju.envs.renju_env import RenjuEnv
from gym_renju.envs.policy.ai import RandomPolicy
from gym_renju.envs.policy.input import InputPolicy
from gym_renju.envs.state.renju_space import RenjuSpace
from gym_renju.envs.utils.generator import BoardStateGenerator as bsg

class RenjuEnvTest(ut.TestCase):

  def setUp(self):
    players = ['input', 'random']
    self.env = RenjuEnv(players, 15, True)

  def test_init(self):
    players = ['input', 'random']
    env = RenjuEnv(players, 15, True)
    self.assertIsInstance(env._policies[PlayerColor.BLACK], InputPolicy)
    self.assertIsInstance(env._policies[PlayerColor.WHITE], RandomPolicy)
    self.assertEquals(RenjuSpace(15*15), env.action_space)
    self.assertEquals(RenjuState(RenjuBoard(15), PlayerColor.WHITE, PlayerColor.BLACK), env._state)

  @patch('gym_renju.envs.policy.ai.RandomPolicy.auto_act')
  @patch('gym_renju.envs.policy.input.InputPolicy.act')
  @patch('gym_renju.envs.policy.input.InputPolicy.auto_act')
  def test_step_auto(self, auto_act_mock, act_mock, ai_auto_act_mock):
    auto_act_mock.return_value = True
    act_mock.return_value = 45
    ai_auto_act_mock.return_value = False
    self.env._step_auto()
    expected_space = RenjuSpace(15*15)
    expected_space.remove(45)
    expected_state = RenjuState(RenjuBoard(15), PlayerColor.WHITE, PlayerColor.BLACK).act(45)
    self.assertIsInstance(self.env._policies[PlayerColor.BLACK], InputPolicy)
    self.assertIsInstance(self.env._policies[PlayerColor.WHITE], RandomPolicy)
    self.assertEquals(expected_space, self.env.action_space)
    self.assertEquals(expected_state, self.env._state)

  @patch('gym_renju.envs.policy.ai.RandomPolicy.act')
  def test_reset(self, act_mock):
    act_mock.return_value = 100
    observation = self.env._reset()
    expected_space = RenjuSpace(15*15)
    expected_space.remove(100)
    expected_state = RenjuState(RenjuBoard(15), PlayerColor.WHITE, PlayerColor.BLACK).act(100)
    expected_observation = np.array([0 for _ in range(15*15)])
    np.put(expected_observation, 100, 1)
    self.assertIsInstance(self.env._policies[PlayerColor.BLACK], RandomPolicy)
    self.assertIsInstance(self.env._policies[PlayerColor.WHITE], InputPolicy)
    self.assertEquals(expected_space, self.env.action_space)
    self.assertEquals(expected_state, self.env._state)
    self.assertTrue(all(expected_observation == observation))

  @patch('gym_renju.envs.renju.RenjuBoard.get_last_action')
  def test_repr_result_lose(self, last_action_mock):
    last_action_mock.return_value = 100
    expected_out = 'Game end on WHITE\'s tern with NONE: last move: 100\nPlayer BLACK Wins!'
    actual_out = self.env._repr_result(Result.LOSE)
    self.assertEquals(expected_out, actual_out)

  @patch('gym_renju.envs.renju.RenjuBoard.get_last_action')
  def test_repr_result_win(self, last_action_mock):
    last_action_mock.return_value = 121
    expected_out = 'Game end on WHITE\'s tern with NONE: last move: 121\nPlayer WHITE Wins!'
    actual_out = self.env._repr_result(Result.WIN)
    self.assertEquals(expected_out, actual_out)

  @patch('gym_renju.envs.renju.RenjuBoard.get_last_action')
  def test_repr_result_draw(self, last_action_mock):
    last_action_mock.return_value = 91

    expected_out = 'Game end on WHITE\'s tern with NONE: last move: 91\nDraw game!'
    actual_out = self.env._repr_result(Result.NONE)
    self.assertEquals(expected_out, actual_out)


  @patch('gym_renju.envs.utils.utils.finish')
  def test_render_not_change_state(self, finish_mock):
    finish_mock.return_value = True
    self.env._render()
    self.assertIsInstance(self.env._policies[PlayerColor.BLACK], InputPolicy)
    self.assertIsInstance(self.env._policies[PlayerColor.WHITE], RandomPolicy)
    self.assertEquals(RenjuSpace(15*15), self.env.action_space)
    self.assertEquals(RenjuState(RenjuBoard(15), PlayerColor.WHITE, PlayerColor.BLACK), self.env._state)

  @patch('gym_renju.envs.policy.ai.RandomPolicy.act')
  def test_step_valid(self, ai_act_mock):
    ai_act_mock.return_value = 191
    actual_observation, actual_reward, actual_is_finish, actual_state_dict = self.env._step(79)
    expected_space = RenjuSpace(15*15)
    expected_space.remove(79)
    expected_space.remove(191)
    expected_state = RenjuState(RenjuBoard(15), PlayerColor.WHITE, PlayerColor.BLACK).act(79).act(191)
    expected_observation = np.array([0 for _ in range(15*15)])
    np.put(expected_observation, [79, 191], [1, 2])
    self.assertIsInstance(self.env._policies[PlayerColor.BLACK], InputPolicy)
    self.assertIsInstance(self.env._policies[PlayerColor.WHITE], RandomPolicy)
    self.assertEquals(expected_space, self.env.action_space)
    self.assertEquals(expected_state, self.env._state)
    self.assertTrue(all(expected_observation == actual_observation))
    self.assertEquals(0, actual_reward)
    self.assertEquals(False, actual_is_finish)
    self.assertEquals({'state': expected_state}, actual_state_dict)

  def test_step_invalid(self):
    with self.assertRaises(error.Error):
      self.env._step(15*15)

  @patch('gym_renju.envs.utils.utils.finish')
  def test_step_finish(self, finsih_mock):
    finsih_mock.return_value = True
    with self.assertRaises(error.Error):
      self.env._step(15*15)

  @patch('gym_renju.envs.rule.renju_reward.ConfiguredReward.get_opponent_reward')
  @patch('gym_renju.envs.rule.renju_reward.ConfiguredReward.get_reward')
  @patch('gym_renju.envs.utils.utils.finish')
  def test_rewards_finished(self, finsih_mock, get_reward_mock, get_opponent_reward_mock):
    finsih_mock.return_value = True
    get_reward_mock.return_value = 10.0
    get_opponent_reward_mock.return_value = -5.0
    rewards = self.env.get_rewards()
    self.assertEquals([-5.0, 10.0], rewards)
    # Also test that the state not changed
    self.assertIsInstance(self.env._policies[PlayerColor.BLACK], InputPolicy)
    self.assertIsInstance(self.env._policies[PlayerColor.WHITE], RandomPolicy)
    self.assertEquals(RenjuSpace(15*15), self.env.action_space)
    self.assertEquals(RenjuState(RenjuBoard(15), PlayerColor.WHITE, PlayerColor.BLACK), self.env._state)

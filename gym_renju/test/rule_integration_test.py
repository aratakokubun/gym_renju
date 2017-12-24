# -*- coding:utf-8 -*-

'''
Integration Test module for rule.
@auther: Arata Kokubun
@data: 2017/12/14
'''

# Imports
import unittest as ut
from parameterized import parameterized

from gym_renju.envs.core.domain.player import PlayerColor
from gym_renju.envs.core.domain.rule_pattern import RulePattern
from gym_renju.envs.rule import rule
from gym_renju.envs.rule.rule_matcher_factory_impl import RuleMatcherFactoryImpl

class JudgeIntegrationTest(ut.TestCase):
  def setUp(self):
    self._board_state = [
        0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1,
        0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1,
        0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0,
        1, 0, 0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0,
    ]
    self._board_size = 15
    self._factory = RuleMatcherFactoryImpl()

  @parameterized.expand([
    [6, RulePattern.YONYON_RYOTO],
    [9, RulePattern.NONE],
    [16, RulePattern.SANSAN],
    [22, RulePattern.NONE],
    [29, RulePattern.NONE],
    [65, RulePattern.TYO_REN],
    [67, RulePattern.NONE],
    [70, RulePattern.YONYON_TYODA],
    [169, RulePattern.YONYON],
    [189, RulePattern.GO_REN],
    [216, RulePattern.NONE],
    [219, RulePattern.YONYON_SORYU],
  ])
  def test_is_pattern_match(self, latest_action: int, result_pattern: RulePattern):
    actual = rule.judge_game(self._factory, self._board_state, self._board_size, PlayerColor.BLACK, latest_action)
    self.assertEqual(result_pattern, actual)

class JudgeDrawIntegrationTest(ut.TestCase):
  def setUp(self):
    self._board_state = [
      1, 1, 1, 2, 2, 2, 1, 1, 1,
      2, 2, 2, 1, 1, 1, 2, 2, 2,
      1, 1, 2, 1, 2, 1, 2, 1, 1,
      1, 1, 1, 2, 2, 2, 1, 1, 1,
      2, 2, 2, 1, 1, 1, 2, 2, 2,
      1, 1, 1, 2, 2, 2, 1, 1, 1,
      2, 2, 2, 1, 1, 1, 2, 2, 2,
      1, 1, 1, 2, 2, 2, 1, 1, 1,
      1, 1, 1, 2, 2, 2, 1, 1, 1,
    ]
    self._board_size = 9
    self._factory = RuleMatcherFactoryImpl()

  def test_is_draw(self):
    actual = rule.judge_game(self._factory, self._board_state, self._board_size, PlayerColor.BLACK, 0)
    self.assertEqual(RulePattern.FULL, actual)

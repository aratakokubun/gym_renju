# -*- coding:utf-8 -*-

'''
Test module for RuleMatcherGenerator.
@auther: Arata Kokubun
@data: 2017/12/16
'''

# Imports
import unittest as ut

from gym_renju.envs.rule.renju_rule_matcher import MatcherAny, MatcherCount

class BoardStateGenerator(ut.TestCase):
  def test_when_any_match_then_true(self):
    matcher = MatcherAny()
    regix = '[0-9]{3}'
    lines = ['abc', '123', '12c']
    self.assertTrue(matcher.call(lines, regix))

  def test_when_no_match_then_false(self):
    matcher = MatcherAny()
    regix = '[0-9]{3}'
    lines = ['abc', '1bc', '12c']
    self.assertFalse(matcher.call(lines, regix))

  def test_when_match_over_then_true(self):
    matcher = MatcherCount(2)
    regix = '[0-9]{3}'
    lines = ['abc', '123', '456']
    self.assertTrue(matcher.call(lines, regix))

  def test_when_match_under_then_false(self):
    matcher = MatcherCount(2)
    regix = '[0-9]{3}'
    lines = ['abc', '123', '12c']
    self.assertFalse(matcher.call(lines, regix))

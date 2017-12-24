# -*- coding:utf-8 -*-

'''
Rule matcher interface module for Renju.
@auther: Arata Kokubun
@date: 2017/12/23
'''

# Imports
from typing import List

from gym_renju.envs.core.domain.rule_pattern import RulePattern

class MatcherCallable(object):
  def call(self, lines: List, regix: str) -> bool:
    raise NotImplementedError

class RuleMatcher(object):
  def match(self, lines: List) -> bool:
    raise NotImplementedError

  def get_rule_pattern(self) -> RulePattern:
    raise NotImplementedError

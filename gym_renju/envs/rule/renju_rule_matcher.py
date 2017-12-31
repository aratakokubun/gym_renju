# -*- coding:utf-8 -*-

'''
Rule matcher module for Renju.
@auther: Arata Kokubun
@date: 2017/12/23
'''

# Imports
import re
from typing import List

from gym_renju.envs.core.domain.rule_pattern import RulePattern
from gym_renju.envs.core.contract.rule_matcher import MatcherCallable, RuleMatcher

class MatcherAny(MatcherCallable):
  def call(self, lines: List, regix: str) -> bool:
    for line in lines:
      if re.search(regix, ''.join(map(str, line))):
        return True
    return False

class MatcherCount(MatcherCallable):
  def __init__(self, min_count):
    self._min_count = min_count

  def call(self, lines: List, regix: str) -> bool:
    count = 0
    for line in lines:
      if re.search(regix, ''.join(map(str, line))):
        count += 1
        if count >= self._min_count:
          return True
    return False

class RegixRuleMatcher(RuleMatcher):
  def __init__(self, rule_pattern: RulePattern, matcher_callable: MatcherCallable,
    regix: str) -> None:
    self._rule_pattern = rule_pattern
    self._matcher_callable = matcher_callable
    self._regix = regix

  def match(self, lines: List) -> bool:
    return self._matcher_callable.call(lines, self._regix)

  def get_rule_pattern(self) -> RulePattern:
    return self._rule_pattern

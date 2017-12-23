# -*- coding:utf-8 -*-

'''
Utility module for generating game states and matchers.
@auther: Arata Kokubun
@data: 2017/12/09
'''

# Imports
import random
import re
from typing import List

from gym_renju.envs.core.domain.player import PlayerColor, PlayerLatest
from gym_renju.envs.core.domain.rule_pattern import RulePattern
from gym_renju.envs.core.contract.space import DiscreteSpace
from gym_renju.envs.core.contract.policy import PlayerPolicy
from gym_renju.envs.policy.ai import RandomPolicy
from gym_renju.envs.policy.input import InputPolicy
from gym_renju.envs.state.renju_space import RenjuSpace
from gym_renju.envs.utils import utils
from gym_renju.envs.utils import rule_pattern_compile as rpc

class BoardStateGenerator(object):
  @staticmethod
  def generate_empty(board_size: int) -> List[int]:
    return [PlayerColor.EMPTY for _ in range(board_size**2)]

  @staticmethod
  def generate_random(board_size: int) -> List[int]:
    return [random.choice(list(PlayerColor)) for _ in range(board_size**2)]

class MatcherCallable(object):
  def call(self, lines: List, regix: str) -> bool:
    raise NotImplementedError

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
          print(regix)
          return True
    return False

class RuleMatcher(object):
  def __init__(self, rule_pattern: RulePattern, matcher_callable: MatcherCallable,
    regix: str) -> None:
    self._rule_pattern = rule_pattern
    self._matcher_callable = matcher_callable
    self._regix = regix

  def match(self, lines: List) -> bool:
    return self._matcher_callable.call(lines, self._regix)

  def get_rule_pattern(self) -> RulePattern:
    return self._rule_pattern

# Constants
WHITE_MATCHERS = [
    RuleMatcher(RulePattern.GO_REN, MatcherAny(),
                rpc.compile_more_go_ren(PlayerColor.WHITE, PlayerLatest.WHITE))]
BLACK_MATCHERS = [
    RuleMatcher(RulePattern.GO_REN, MatcherAny(),
                rpc.compile_go_ren(PlayerColor.BLACK, PlayerLatest.BLACK)),
    RuleMatcher(RulePattern.TYO_REN, MatcherAny(),
                rpc.compile_tyo_ren(PlayerColor.BLACK, PlayerLatest.BLACK)),
    RuleMatcher(RulePattern.YONYON_RYOTO, MatcherAny(),
                rpc.compile_yonyon_ryoto(PlayerColor.BLACK, PlayerLatest.BLACK)),
    RuleMatcher(RulePattern.YONYON_TYODA, MatcherAny(),
                rpc.compile_yonyon_tyoda(PlayerColor.BLACK, PlayerLatest.BLACK)),
    RuleMatcher(RulePattern.YONYON_SORYU, MatcherAny(),
                rpc.compile_yonyon_soryu(PlayerColor.BLACK, PlayerLatest.BLACK)),
    RuleMatcher(RulePattern.SANSAN, MatcherCount(2),
                rpc.compile_san(PlayerColor.BLACK, PlayerLatest.BLACK)),
    RuleMatcher(RulePattern.YONYON, MatcherCount(2),
                rpc.compile_yon(PlayerColor.BLACK, PlayerLatest.BLACK))]

class RuleMatcherGenerator(object):
  @staticmethod
  def generate(player_color: PlayerColor):
    assert player_color in utils.valid_player_colors()
    if player_color is PlayerColor.BLACK:
      return BLACK_MATCHERS
    elif player_color is PlayerColor.WHITE:
      return WHITE_MATCHERS

class DiscreteSpaceGenerator(object):
  @staticmethod
  def generate(space_size: int) -> DiscreteSpace:
    return RenjuSpace(space_size)

class RnejuPlayerGenerator(object):
  @staticmethod
  def generate(policy: str) -> PlayerPolicy:
    if policy == 'input':
      return InputPolicy()
    elif policy == 'random':
      return RandomPolicy()

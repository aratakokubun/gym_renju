# -*- coding:utf-8 -*-

'''
Implemented factory module for Renju rule matcher.
@auther: Arata Kokubun
@date: 2017/12/23
'''

# Imports
from typing import List

from gym_renju.envs.core.domain.player import PlayerColor, PlayerLatest
from gym_renju.envs.core.domain.rule_pattern import RulePattern
from gym_renju.envs.core.contract.rule_matcher import RuleMatcher
from gym_renju.envs.core.contract.factory import RuleMatcherFactory
from gym_renju.envs.utils import utils
from gym_renju.envs.utils import rule_pattern_compile as rpc
from gym_renju.envs.rule.renju_rule_matcher import MatcherAny, MatcherCount, RegixRuleMatcher

# Constants
WHITE_MATCHERS = [
    RegixRuleMatcher(RulePattern.GO_REN, MatcherAny(),
                rpc.compile_more_go_ren(PlayerColor.WHITE, PlayerLatest.WHITE))]
BLACK_MATCHERS = [
    RegixRuleMatcher(RulePattern.GO_REN, MatcherAny(),
                rpc.compile_go_ren(PlayerColor.BLACK, PlayerLatest.BLACK)),
    RegixRuleMatcher(RulePattern.TYO_REN, MatcherAny(),
                rpc.compile_tyo_ren(PlayerColor.BLACK, PlayerLatest.BLACK)),
    RegixRuleMatcher(RulePattern.YONYON_RYOTO, MatcherAny(),
                rpc.compile_yonyon_ryoto(PlayerColor.BLACK, PlayerLatest.BLACK)),
    RegixRuleMatcher(RulePattern.YONYON_TYODA, MatcherAny(),
                rpc.compile_yonyon_tyoda(PlayerColor.BLACK, PlayerLatest.BLACK)),
    RegixRuleMatcher(RulePattern.YONYON_SORYU, MatcherAny(),
                rpc.compile_yonyon_soryu(PlayerColor.BLACK, PlayerLatest.BLACK)),
    RegixRuleMatcher(RulePattern.SANSAN, MatcherCount(2),
                rpc.compile_san(PlayerColor.BLACK, PlayerLatest.BLACK)),
    RegixRuleMatcher(RulePattern.YONYON, MatcherCount(2),
                rpc.compile_yon(PlayerColor.BLACK, PlayerLatest.BLACK))]

class RuleMatcherFactoryImpl(RuleMatcherFactory):
  def generate(self, player_color: PlayerColor) -> List[RuleMatcher]:
    assert player_color in utils.valid_player_colors()
    if player_color is PlayerColor.BLACK:
      return BLACK_MATCHERS
    elif player_color is PlayerColor.WHITE:
      return WHITE_MATCHERS

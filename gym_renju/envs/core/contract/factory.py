# -*- coding:utf-8 -*-

'''
Factory interface module for contracts.
@auther: Arata Kokubun
@date: 2017/12/23
'''

# Imports
from typing import List

from gym_renju.envs.core.domain.player import PlayerColor
from gym_renju.envs.core.contract.policy import PlayerPolicy
from gym_renju.envs.core.contract.reward import Reward
from gym_renju.envs.core.contract.rule_matcher import RuleMatcher
from gym_renju.envs.core.contract.space import DiscreteSpace

class PlayerPolicyFactory(object):
  def generate(self, policy: str) -> PlayerPolicy:
    raise NotImplementedError

class RewardFactory(object):
  def generate(self) -> Reward:
    raise NotImplementedError

class RuleMatcherFactory(object):
  def generate(self, player_color: PlayerColor) -> List[RuleMatcher]:
    raise NotImplementedError

class DiscreteSpaceFactory(object):
  def generate(self, space_size: int) -> DiscreteSpace:
    raise NotImplementedError

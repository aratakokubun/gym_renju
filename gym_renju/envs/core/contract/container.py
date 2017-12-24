# -*- coding:utf-8 -*-

'''
Container interface module for factory contracts.
@auther: Arata Kokubun
@date: 2017/12/23
'''

# Imports
from gym_renju.envs.core.contract.factory import PlayerPolicyFactory, RewardFactory,\
  RuleMatcherFactory, DiscreteSpaceFactory

class Container(object):
  def get_policy_factory(self) -> PlayerPolicyFactory:
    raise NotImplementedError

  def get_reward_factory(self) -> RewardFactory:
    raise NotImplementedError

  def get_rule_matcher_factory(self) -> RuleMatcherFactory:
    raise NotImplementedError

  def get_space_factory(self) -> DiscreteSpaceFactory:
    raise NotImplementedError

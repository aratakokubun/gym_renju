# -*- coding:utf-8 -*-

'''
DI container module for Renju.
@auther: Arata Kokubun
@date: 2017/12/24
'''

# Imports
from injector import inject, Injector, Module, singleton

from gym_renju.envs.core.contract.container import Container
from gym_renju.envs.core.contract.factory import PlayerPolicyFactory, RewardFactory,\
  RuleMatcherFactory, DiscreteSpaceFactory
from gym_renju.envs.policy.policy_factory_impl import PolicyFactoryImpl
from gym_renju.envs.rule.reward_factory_impl import RewardFactoryImpl
from gym_renju.envs.rule.rule_matcher_factory_impl import RuleMatcherFactoryImpl
from gym_renju.envs.state.space_factory_impl import DiscreteSpaceFactoryImpl

class RenjuContainer(Container):
  @inject
  def __init__(self, policy_factory: PlayerPolicyFactory, reward_factory: RewardFactory,
    rule_matcher_factory: RuleMatcherFactory, space_factory: DiscreteSpaceFactory):
    self._policy_factory = policy_factory
    self._reward_factory = reward_factory
    self._rule_matcher_factory = rule_matcher_factory
    self._space_factory = space_factory

  def get_policy_factory(self) -> PlayerPolicyFactory:
    return self._policy_factory

  def get_reward_factory(self) -> RewardFactory:
    return self._reward_factory

  def get_rule_matcher_factory(self) -> RuleMatcherFactory:
    return self._rule_matcher_factory

  def get_space_factory(self) -> DiscreteSpaceFactory:
    return self._space_factory

class RenjuDiModule(Module):
  '''
  DI module for normal renju game
  '''
  def configure(self, binder):
    binder.bind(PlayerPolicyFactory, to=PolicyFactoryImpl, scope=singleton)
    binder.bind(RewardFactory, to=RewardFactoryImpl, scope=singleton)
    binder.bind(RuleMatcherFactory, to=RuleMatcherFactoryImpl, scope=singleton)
    binder.bind(DiscreteSpaceFactory, to=DiscreteSpaceFactoryImpl, scope=singleton)

def compile_container() -> Container:
  __injector = Injector([RenjuDiModule()])
  return __injector.get(RenjuContainer)

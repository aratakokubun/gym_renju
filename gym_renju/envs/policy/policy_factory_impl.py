# -*- coding:utf-8 -*-

'''
Implemented factory module for Renju policy.
@auther: Arata Kokubun
@date: 2017/12/23
'''

# Imports
from gym_renju.envs.core.contract.policy import PlayerPolicy
from gym_renju.envs.core.contract.factory import PlayerPolicyFactory
from gym_renju.envs.policy.ai import RandomPolicy
from gym_renju.envs.policy.input import InputPolicy
from gym_renju.envs.exception.invalid_type_exception import InvalidPolicyException

class PolicyFactoryImpl(PlayerPolicyFactory):
  def generate(self, policy: str) -> PlayerPolicy:
    if policy == 'input':
      return InputPolicy()
    elif policy == 'random':
      return RandomPolicy()
    else:
      raise InvalidPolicyException(policy)

# -*- coding:utf-8 -*-

'''
Test module for Policy factory.
@auther: Arata Kokubun
@data: 2017/12/23
'''

# Imports
import unittest as ut
from parameterized import parameterized

from gym_renju.envs.policy.ai import RandomPolicy
from gym_renju.envs.policy.input import InputPolicy
from gym_renju.envs.policy.policy_factory_impl import PolicyFactoryImpl
from gym_renju.envs.exception.invalid_type_exception import InvalidPolicyException

class PolicyFactoryTest(ut.TestCase):
  def setUp(self):
    self._policy_factory = PolicyFactoryImpl()

  @parameterized.expand([['input', InputPolicy], ['random', RandomPolicy]])
  def test_generate_valid_policy(self, policy: str, clazz: type):
    actual = self._policy_factory.generate(policy)
    self.assertEqual(clazz, type(actual))

  def test_generate_invalid_policy(self):
    with self.assertRaises(InvalidPolicyException):
      self._policy_factory.generate('invalid')

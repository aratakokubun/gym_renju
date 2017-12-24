# -*- coding:utf-8 -*-

'''
Implemented factory module for gym space.
@auther: Arata Kokubun
@date: 2017/12/23
'''

# Imports
from gym_renju.envs.core.contract.space import DiscreteSpace
from gym_renju.envs.core.contract.factory import DiscreteSpaceFactory
from gym_renju.envs.state.renju_space import RenjuSpace

class DiscreteSpaceFactoryImpl(DiscreteSpaceFactory):
  def generate(self, space_size: int) -> DiscreteSpace:
    return RenjuSpace(space_size)

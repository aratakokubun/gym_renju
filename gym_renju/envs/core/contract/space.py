# -*- coding:utf-8 -*-

'''
Space interface module for Renju.
@auther: Arata Kokubun
@data: 2017/12/23
'''

# Imports
from gym.spaces import Discrete

class DiscreteSpace(Discrete):
  def remove(self, action: int):
    raise NotImplementedError

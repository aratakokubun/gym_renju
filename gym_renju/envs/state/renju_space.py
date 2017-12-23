# -*- coding:utf-8 -*-

'''
Wrapper module for action space.
@auther: Arata Kokubun
@data: 2017/12/23
'''

# Imports
from typing import List
from gym.utils import seeding

from gym_renju.envs.core.contract.space import DiscreteSpace

class RenjuSpace(DiscreteSpace):
  def __init__(self, n):
    super().__init__(n)
    self.valid_spaces = list(range(n))

  def sample(self) -> List[int]:
    '''Only sample from the remaining valid spaces
    '''
    if not self.valid_spaces:
      print("Space is empty")
      return None
    np_random, _ = seeding.np_random()
    randint = np_random.randint(len(self.valid_spaces))
    return self.valid_spaces[randint]

  def remove(self, action: int):
    '''Remove space s from the valid spaces
    '''
    if action is None:
      return
    if action in self.valid_spaces:
      self.valid_spaces.remove(action)
    else:
      print("space %d is not in valid spaces" % action)

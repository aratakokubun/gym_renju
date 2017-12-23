# -*- coding:utf-8 -*-

'''
Input player module for Renju.
@auther: Arata Kokubun
@data: date
'''

# Imports
from gym_renju.envs.core.contract.policy import PlayerPolicy

class InputPolicy(PlayerPolicy):
  '''
  Policy for input programmed by library user
  '''
  def auto_act(self) -> bool:
    return False
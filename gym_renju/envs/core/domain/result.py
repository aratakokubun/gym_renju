# -*- coding:utf-8 -*-

'''
Result domain object module.
@auther: Arata Kokubun
@data: 2017/12/16
'''

# Imports
from enum import Enum

class Result(Enum):
  NONE = 0
  WIN = 1
  LOSE = 2
  DRAW = 3
  RESET = 4
  
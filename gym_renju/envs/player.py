# -*- coding:utf-8 -*-

'''
Player enum module.
@auther: Arata Kokubun
@data: 2017/12/09
'''

# Imports
from enum import Enum

class PlayerType(Enum):
  INPUT = 'input'
  RANDOM = 'random'
  BEGINNER = 'beginner'
  INTERMEDIATE = 'intermediate'

class PlayerColor(Enum):
  EMPTY = 0
  BLACK = 1
  WHITE = 2

class PlayerLatest(Enum):
  BLACK = 3
  WHITE = 4

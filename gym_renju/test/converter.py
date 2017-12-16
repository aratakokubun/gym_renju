# -*- coding:utf-8 -*-

'''
Converter model for unit test.
@auther: Arata Kokubun
@data: 2017/12/16
'''

# Imports
from typing import List
from gym_renju.envs.domain.player import PlayerColor

def convert_board(board: List[int]) -> List[PlayerColor]:
  return list(map(lambda n: PlayerColor(n), board))

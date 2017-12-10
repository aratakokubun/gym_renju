# -*- coding:utf-8 -*-

'''
Invalid type exception module.
@auther: Arata Kokubun
@data: 2017/12/09
'''

from gym_renju.envs.player import PlayerColor, PlayerType

class InvalidPlayerColorException(Exception):
  def __init__(self, player_color: PlayerColor) -> None:
    self._player_color = player_color

  def __str__(self) -> str:
    return 'Player color {0} is not allowed.'.format(self._player_color)

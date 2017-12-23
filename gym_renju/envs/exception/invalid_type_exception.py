# -*- coding:utf-8 -*-

'''
Invalid type exception module.
@auther: Arata Kokubun
@data: 2017/12/09
'''

from gym_renju.envs.core.domain.player import PlayerColor

class InvalidPlayerColorException(Exception):
  def __init__(self, player_color: PlayerColor) -> None:
    super().__init__()
    self._player_color = player_color

  def __str__(self) -> str:
    return 'Player color {0} is not allowed.'.format(self._player_color)

class InvalidPolicyException(Exception):
  def __init__(self, policy: str) -> None:
    super().__init__()
    self._policy = policy

  def __str__(self) -> str:
    return 'Policy {0} is not allowed.'.format(self._policy)

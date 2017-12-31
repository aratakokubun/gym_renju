# -*- coding:utf-8 -*-

'''
Rule pattern compiler modules.
@auther: Arata Kokubun
@data: 20171210
'''

from typing import Dict
from functools import reduce
import itertools as it

from gym_renju.envs.core.domain.player import PlayerColor, PlayerLatest

def combination_match(patterns: Dict) -> str:
  '''
  generate combination of regex pattern match string.
  @param pattern: Dictionary of pattern(str): count(int)
  '''
  seq = reduce(lambda x, y: x+y, [[key]*value for key, value in patterns.items()])
  return reduce(lambda x, y: ''.join(x) + '|' + ''.join(y), set(it.permutations(seq)))

GO_REN = '(?:^|[^{0}{1}])(' + combination_match({'{0}':4, '{1}':1}) + ')(?=(?:$|[^{0}{1}]))'
MORE_GO_REN = combination_match({'{0}':4, '{1}':1})
TYO_REN = combination_match({'{0}':5, '{1}':1})
TASSHI = '(?:^|[^{0}{2}]){1}(' + combination_match({'{0}':3, '{2}':1}) + ')(?={1}(?:$|[^{0}{2}]))'
YON = '(?:^|[^{0}{2}])(' + combination_match({'{0}':3, '{1}':1, '{2}':1}) + ')(?=(?:$|[^{0}{2}]))'
YONYON_RYOTO = '(?:^|[^{0}]){0}{1}(' + combination_match({'{0}':2, '{2}':1}) + '){1}{0}(?=(?:$|[^{0}]))'
YONYON_TYODA = '(?:^|[^{0}]){0}{{2}}{1}({0}{2}|{2}{0}){1}{0}{{2}}(?=(?:$|[^{0}]))'
YONYON_SORYU = '(?:^|[^{0}]){0}{{3}}{1}{2}{1}{0}{{3}}(?=(?:$|[^{0}]))'
SAN = '(?:^|[^{0}{2}]){1}(' + combination_match({'{0}':2, '{1}':1, '{2}':1}) + ')(?={1}(?:$|[^{0}{2}]))'

def compile_go_ren(player_color: PlayerColor, player_latest: PlayerLatest) -> Dict:
  return GO_REN.format(player_color.value, player_latest.value)

def compile_more_go_ren(player_color: PlayerColor, player_latest: PlayerLatest) -> Dict:
  return MORE_GO_REN.format(player_color.value, player_latest.value)

def compile_tyo_ren(player_color: PlayerColor, player_latest: PlayerLatest) -> Dict:
  return TYO_REN.format(player_color.value, player_latest.value)

def compile_tasshi(player_color: PlayerColor, player_latest: PlayerLatest) -> Dict:
  return TASSHI.format(player_color.value, PlayerColor.EMPTY.value, player_latest.value)

def compile_yon(player_color: PlayerColor, player_latest: PlayerLatest) -> Dict:
  return YON.format(player_color.value, PlayerColor.EMPTY.value, player_latest.value)

def compile_yonyon_ryoto(player_color: PlayerColor, player_latest: PlayerLatest) -> Dict:
  return YONYON_RYOTO.format(player_color.value, PlayerColor.EMPTY.value, player_latest.value)

def compile_yonyon_tyoda(player_color: PlayerColor, player_latest: PlayerLatest) -> Dict:
  return YONYON_TYODA.format(player_color.value, PlayerColor.EMPTY.value, player_latest.value)

def compile_yonyon_soryu(player_color: PlayerColor, player_latest: PlayerLatest) -> Dict:
  return YONYON_SORYU.format(player_color.value, PlayerColor.EMPTY.value, player_latest.value)

def compile_san(player_color: PlayerColor, player_latest: PlayerLatest) -> Dict:
  return SAN.format(player_color.value, PlayerColor.EMPTY.value, player_latest.value)

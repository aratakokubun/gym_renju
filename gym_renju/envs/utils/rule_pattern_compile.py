# -*- coding:utf-8 -*-

'''
Rule pattern compiler modules.
@auther: Arata Kokubun
@data: 20171210
'''

from typing import Dict
from gym_renju.envs.player import PlayerColor, PlayerLatest

GO_REN = '(?:^|[^{0}]){0}{{5}}(?=(?:$|[^{0}]))'
TYO_REN = '[{0}{1}]{{6}}'
TASSHI = '(?:^|[^{0}]){1}{0}{{4}}(?={1}(?:$|[^{0}]))'
YON = '(?:^|[^{0}])([{0}{2}]{{4}}{1}|[{0}{2}]{{3}}{1}[{0}{2}]|[{0}{2}]{{2}}{1}[{0}{2}]{{2}}|[{0}{2}]{1}[{0}{2}]{{3}}|{1}[{0}{2}]{{4}})(?=(?:$|[^{0}]))'
YONYON_RYOTO = '(?:^|[^{0}]){0}{1}({0}{{2}}{2}|{0}{2}{0}|{2}{0}{{2}}){1}{0}(?=(?:$|[^{0}]))'
YONYON_TYODA = '(?:^|[^{0}]){0}{{2}}{1}({0}{2}|{2}{0}){1}{0}{{2}}(?=(?:$|[^{0}]))'
YONYON_SORYU = '(?:^|[^{0}]){0}{{3}}{1}{2}{1}{0}{{3}}(?=(?:$|[^{0}]))'
SAN = '(?:^|[^{0}]){1}([{0}{2}]{{3}}{1}|[{0}{2}]{{2}}{1}[{0}{2}]|[{0}{2}]{1}[{0}{2}]{{2}}|{1}[{0}{2}]{{3}}){1}(?=(?:$|[^{0}]))'

def compile_go_ren(player_color: PlayerColor) -> Dict:
  return GO_REN.format(player_color.value)

def compile_tyo_ren(player_color: PlayerColor, player_latest: PlayerLatest) -> Dict:
  return TYO_REN.format(player_color.value, player_latest)

def compile_tasshi(player_color: PlayerColor) -> Dict:
  return TASSHI.format(player_color.value, PlayerColor.EMPTY.value)

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

# -*- coding:utf-8 -*-

'''
Rule pattern compiler modules.
@auther: Arata Kokubun
@data: 20171210
'''

import re
from enum import Enum
from typing import Dict
from gym_renju.envs.player import PlayerColor, PlayerLatest

class SpecialPatterns(Enum):
  GO_REN = 'go_ren'
  TYO_REN = 'tyo_ren'
  TASSHI = 'tasshi'
  YON = 'yon'
  YONYON_RYOTO = 'yonyon_ryoto'
  YONYON_TYODA = 'yonyon_tyoda'
  YONYON_SORYU = 'yonyon_soryu'
  SAN = 'san'

GO_REN = '(?:^|[^{0}]){0}{{5}}(?=(?:$|[^{0}]))'
TYO_REN = '{0}{{6}}'
TASSHI = '(?:^|[^{0}]){1}{0}{{4}}(?={1}(?:$|[^{0}]))'
YON = '(?:^|[^{0}])({0}{{4}}{1}|{0}{{3}}{1}{0}|{0}{{2}}{1}{0}{{2}}|{0}{1}{0}{{3}}|{1}{0}{{4}})(?=(?:$|[^{0}]))'
YONYON_RYOTO = '(?:^|[^{0}]){0}{1}({0}{{2}}{2}|{0}{2}{0}|{2}{0}{{2}}){1}{0}(?=(?:$|[^{0}]))'
YONYON_TYODA = '(?:^|[^{0}]){0}{{2}}{1}({0}{2}|{2}{0}){1}{0}{{2}}(?=(?:$|[^{0}]))'
YONYON_SORYU = '(?:^|[^{0}]){0}{{3}}{1}{2}{1}{0}{{3}}(?=(?:$|[^{0}]))'
SAN = '(?:^|[^{0}]){1}({0}{{3}}{1}|{0}{{2}}{1}{0}|{0}{1}{0}{{2}}|{1}{0}{{3}}){1}(?=(?:$|[^{0}]))'

def pcompile(player_color: PlayerColor, player_latest: PlayerLatest) -> Dict:
  patterns = dict()
  patterns[SpecialPatterns.GO_REN] = GO_REN.format(player_color.value)
  patterns[SpecialPatterns.TYO_REN] = TYO_REN.format(player_color.value)
  patterns[SpecialPatterns.TASSHI] = TASSHI.format(player_color.value, PlayerColor.EMPTY.value)
  patterns[SpecialPatterns.YON] = YON.format(player_color.value, PlayerColor.EMPTY.value)
  patterns[SpecialPatterns.YONYON_RYOTO] = YONYON_RYOTO.format(player_color.value, PlayerColor.EMPTY.value, player_latest.value)
  patterns[SpecialPatterns.YONYON_TYODA] = YONYON_TYODA.format(player_color.value, PlayerColor.EMPTY.value, player_latest.value)
  patterns[SpecialPatterns.YONYON_SORYU] = YONYON_SORYU.format(player_color.value, PlayerColor.EMPTY.value, player_latest.value)
  patterns[SpecialPatterns.SAN] = SAN.format(player_color.value, PlayerColor.EMPTY.value)
  return patterns

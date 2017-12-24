# -*- coding:utf-8 -*-

'''
Rule pattern domain object module.
@auther: Arata Kokubun
@data: 2017/12/16
'''

# Imports
from enum import Enum

class RulePattern(Enum):
  GO_REN = "5-ren"
  TYO_REN = "tyo-ren"
  YONYON_RYOTO = "yonyon-ryoto"
  YONYON_TYODA = "yonyon-tyoda"
  YONYON_SORYU = "yonyon-soryu"
  YONYON = "yonyon"
  SANSAN = "sansan"
  NONE = "none"
  FULL = "full"

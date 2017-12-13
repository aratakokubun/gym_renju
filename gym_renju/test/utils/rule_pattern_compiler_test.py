# -*- coding:utf-8 -*-

'''
Test module for rule pattern compiler.
@auther: Arata Kokubun
@data: 2017/12/10
'''

# Imports
import unittest as ut
import re
from parameterized import parameterized
from gym_renju.envs.player import PlayerColor, PlayerLatest
from gym_renju.envs.utils import rule_pattern_compile as rpc

class RulePatternCompilerTest(ut.TestCase):
  @parameterized.expand([
    # color, latest, pattern_name, pattern, match_nums
    [PlayerColor.BLACK, '0111112', 1],
    [PlayerColor.WHITE, '122222', 1],
    [PlayerColor.BLACK, '111110', 1],
    [PlayerColor.WHITE, '22222', 1],
    [PlayerColor.BLACK, '11111011111', 2],
    [PlayerColor.BLACK, '1111112', 0],
    [PlayerColor.BLACK, '1111', 0],
    [PlayerColor.BLACK, '2112110', 0]])
  def test_go_ren(self, player_color: PlayerColor, pattern: str, match_nums: int):
    re_pattern = rpc.compile_go_ren(player_color)
    matched = re.findall(re_pattern, pattern)
    self.assertEqual(len(matched), match_nums)

  @parameterized.expand([
    # color, latest, pattern_name, pattern, match_nums
    [PlayerColor.BLACK, PlayerLatest.BLACK, '111111', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '11111110111111', 2],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0111112', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '111101111', 0]])
  def test_tyo_ren(self, player_color: PlayerColor, player_latest: PlayerLatest,
    pattern: str, match_nums: int):
    re_pattern = rpc.compile_tyo_ren(player_color, player_latest)
    matched = re.findall(re_pattern, pattern)
    self.assertEqual(len(matched), match_nums)

  @parameterized.expand([
    # color, latest, pattern_name, pattern, match_nums
    [PlayerColor.BLACK, '00111102', 1],
    [PlayerColor.BLACK, '011110', 1],
    [PlayerColor.BLACK, '011110011110', 2],
    [PlayerColor.BLACK, '00111120', 0],
    [PlayerColor.BLACK, '02111100', 0],
    [PlayerColor.BLACK, '001111100', 0],
    [PlayerColor.BLACK, '10111110', 0],
    [PlayerColor.BLACK, '00110100', 0]])
  def test_tasshi(self, player_color: PlayerColor, pattern: str, match_nums: int):
    re_pattern = rpc.compile_tasshi(player_color)
    matched = re.findall(re_pattern, pattern)
    self.assertEqual(len(matched), match_nums)

  @parameterized.expand([
    # color, latest, pattern_name, pattern, match_nums
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0111102', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0111012', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0110112', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0101112', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0011112', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '11110', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '11110010111', 2],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0111110', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '01110110', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0111101', 1]])
  def test_yon(self, player_color: PlayerColor, player_latest: PlayerLatest,
    pattern: str, match_nums: int):
    re_pattern = rpc.compile_yon(player_color, player_latest)
    matched = re.findall(re_pattern, pattern)
    self.assertEqual(len(matched), match_nums)

  @parameterized.expand([
    # color, latest, pattern_name, pattern, match_nums
    [PlayerColor.BLACK, PlayerLatest.BLACK, '010113012', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '1013101', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '1031101', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '21011301010131012', 2],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '010113011', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '010111012', 0],
    [PlayerColor.BLACK, PlayerLatest.WHITE, '010113012', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '010113212', 0]])
  def test_yonyon_ryoto(self, player_color: PlayerColor, player_latest: PlayerLatest,
    pattern: str, match_nums: int):
    re_pattern = rpc.compile_yonyon_ryoto(player_color, player_latest)
    matched = re.findall(re_pattern, pattern)
    self.assertEqual(len(matched), match_nums)

  @parameterized.expand([
    # color, latest, pattern_name, pattern, match_nums
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0110130112', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '11031011', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0110130112110310110', 2],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0110130111', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0110110112', 0],
    [PlayerColor.BLACK, PlayerLatest.WHITE, '0110130112', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0112130110', 0]])
  def test_yonyon_tyoda(self, player_color: PlayerColor, player_latest: PlayerLatest,
    pattern: str, match_nums: int):
    re_pattern = rpc.compile_yonyon_tyoda(player_color, player_latest)
    matched = re.findall(re_pattern, pattern)
    self.assertEqual(len(matched), match_nums)

  @parameterized.expand([
    # color, latest, pattern_name, pattern, match_nums
    [PlayerColor.BLACK, PlayerLatest.BLACK, '01110301112', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '111030111', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '011103011121110301112', 2],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '01110301111', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '01110101110', 0],
    [PlayerColor.BLACK, PlayerLatest.WHITE, '01110301110', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '01112301110', 0]])
  def test_yonyon_soryu(self, player_color: PlayerColor, player_latest: PlayerLatest,
    pattern: str, match_nums: int):
    re_pattern = rpc.compile_yonyon_soryu(player_color, player_latest)
    matched = re.findall(re_pattern, pattern)
    self.assertEqual(len(matched), match_nums)

  @parameterized.expand([
    # color, latest, pattern_name, pattern, match_nums
    [PlayerColor.BLACK, PlayerLatest.BLACK, '00111002', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0110102', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '2010110', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '001110', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0011102011010', 2],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '001111002', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '001121002', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0011101', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '02111002', 0]])
  def test_san(self, player_color: PlayerColor, player_latest: PlayerLatest,
    pattern: str, match_nums: int):
    re_pattern = rpc.compile_san(player_color, player_latest)
    matched = re.findall(re_pattern, pattern)
    self.assertEqual(len(matched), match_nums)

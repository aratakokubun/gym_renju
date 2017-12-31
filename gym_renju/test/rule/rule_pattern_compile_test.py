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

from gym_renju.envs.core.domain.player import PlayerColor, PlayerLatest
from gym_renju.envs.utils import rule_pattern_compile as rpc

class CombinationMatchTest(ut.TestCase):
  def test_combination(self):
    patterns = {'{0}':3, '{1}':1, '{2}': 1}
    expected_strs = [
      '{1}{2}{0}{0}{0}', '{1}{0}{2}{0}{0}', '{1}{0}{0}{2}{0}', '{1}{0}{0}{0}{2}',
      '{2}{1}{0}{0}{0}', '{0}{1}{2}{0}{0}', '{0}{1}{0}{2}{0}', '{0}{1}{0}{0}{2}',
      '{2}{0}{1}{0}{0}', '{0}{2}{1}{0}{0}', '{0}{0}{1}{2}{0}', '{0}{0}{0}{1}{2}',
      '{2}{0}{0}{1}{0}', '{0}{2}{0}{1}{0}', '{0}{0}{2}{1}{0}', '{0}{0}{0}{1}{2}',
      '{2}{0}{0}{0}{1}', '{0}{2}{0}{0}{1}', '{0}{0}{2}{0}{1}', '{0}{0}{0}{2}{1}',
    ]
    expected_length = sum(len(expected) for expected in expected_strs) + len(expected_strs) - 1
    actual = rpc.combination_match(patterns)
    self.assertEqual(expected_length, len(actual))
    self.assertTrue(all(expected in actual for expected in expected_strs))

class RulePatternCompilerTest(ut.TestCase):
  @parameterized.expand([
    # color, latest, pattern_name, pattern, match_nums
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0131112', 1],
    [PlayerColor.WHITE, PlayerLatest.WHITE, '122422', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '111130', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '111310', 1],
    [PlayerColor.WHITE, PlayerLatest.WHITE, '42222', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '11113031111', 2],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '111110', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '3111110', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '011131120', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '1131', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '2132110', 0]])
  def test_go_ren(self, player_color: PlayerColor, player_latest: PlayerLatest,
    pattern: str, match_nums: int):
    re_pattern = rpc.compile_go_ren(player_color, player_latest)
    matched = re.findall(re_pattern, pattern)
    self.assertEqual(match_nums, len(matched))

  @parameterized.expand([
    # color, latest, pattern_name, pattern, match_nums
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0311112', 1],
    [PlayerColor.WHITE, PlayerLatest.WHITE, '122224', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '113110', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '111310', 1],
    [PlayerColor.WHITE, PlayerLatest.WHITE, '22422', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '11113031111', 2],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '3111110', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '011111320', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '111110', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '1131', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '2312110', 0]])
  def test_more_go_ren(self, player_color: PlayerColor, player_latest: PlayerLatest,
    pattern: str, match_nums: int):
    re_pattern = rpc.compile_more_go_ren(player_color, player_latest)
    matched = re.findall(re_pattern, pattern)
    self.assertEqual(match_nums, len(matched))

  @parameterized.expand([
    # color, latest, pattern_name, pattern, match_nums
    [PlayerColor.BLACK, PlayerLatest.BLACK, '311111', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '111311', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '11111130311111', 2],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '111111', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0131112', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '111301131', 0]])
  def test_tyo_ren(self, player_color: PlayerColor, player_latest: PlayerLatest,
    pattern: str, match_nums: int):
    re_pattern = rpc.compile_tyo_ren(player_color, player_latest)
    matched = re.findall(re_pattern, pattern)
    self.assertEqual(match_nums, len(matched))

  @parameterized.expand([
    # color, latest, pattern_name, pattern, match_nums
    [PlayerColor.BLACK, PlayerLatest.BLACK, '00311102', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '011310', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '013110', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '011130031110', 2],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '011110', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0111130', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '00131120', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '02113100', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '001131100', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '10111310', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '00130100', 0]])
  def test_tasshi(self, player_color: PlayerColor, player_latest: PlayerLatest,
    pattern: str, match_nums: int):
    re_pattern = rpc.compile_tasshi(player_color, player_latest)
    matched = re.findall(re_pattern, pattern)
    self.assertEqual(match_nums, len(matched))

  @parameterized.expand([
    # color, latest, pattern_name, pattern, match_nums
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0311102', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0131012', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0110132', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0103112', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0011312', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '31110', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '11310030111', 2],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0111102', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0311110', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0111110', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '01110110', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0113101', 1]])
  def test_yon(self, player_color: PlayerColor, player_latest: PlayerLatest,
    pattern: str, match_nums: int):
    re_pattern = rpc.compile_yon(player_color, player_latest)
    matched = re.findall(re_pattern, pattern)
    self.assertEqual(match_nums, len(matched))

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
    self.assertEqual(match_nums, len(matched))

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
    self.assertEqual(match_nums, len(matched))

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
    self.assertEqual(match_nums, len(matched))

  @parameterized.expand([
    # color, latest, pattern_name, pattern, match_nums
    [PlayerColor.BLACK, PlayerLatest.BLACK, '00113002', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0110302', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '2030110', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '2010310', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '001310', 1],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0011302031010', 2],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '003110011030', 2],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '00111002', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0011103', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '001311002', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '001321002', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '0013101', 0],
    [PlayerColor.BLACK, PlayerLatest.BLACK, '02113002', 0]])
  def test_san(self, player_color: PlayerColor, player_latest: PlayerLatest,
    pattern: str, match_nums: int):
    re_pattern = rpc.compile_san(player_color, player_latest)
    matched = re.findall(re_pattern, pattern)
    self.assertEqual(match_nums, len(matched))

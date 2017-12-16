# -*- coding:utf-8 -*-

'''
Rule definition modules for Renju Game .
@auther: Arata Kokubun
@data: 2017/12/04
'''

from typing import List, Tuple
import operator
import re

from gym_renju.envs.domain.player import PlayerColor, PlayerLatest
from gym_renju.envs.utils import utils
from gym_renju.envs.utils import rule_pattern_compile as rpc
from gym_renju.envs.utils.rule_pattern_compile import RulePattern

def search_sequence(board_state: List[int], start: int, search_dir: Tuple, size: int) -> List:
  '''
  Search sequencial color in the board.
  @param board_state: board to search from
  @param start: search start index
  @param search_dir: search direction
  @param size: board size
  @return pair of (number of sequence, color)
  '''
  color = board_state[start]
  to_next = lambda c: tuple(map(operator.add, c, search_dir))
  in_range = lambda c: 0 <= c[0] < size and 0 <= c[1] < size
  next_coords = to_next(utils.index_to_coords(start, size))
  count = 1
  while in_range(next_coords):
    if color is board_state[utils.coords_to_index(next_coords, size)]:
      count += 1
      next_coords = to_next(next_coords)
    else:
      break
  return (count, color)

def match_pattern(lines: List[int], pattern: str) -> bool:
  for line in lines:
    if re.search(pattern, ''.join(map(str, line))):
      return True
  return False

def match_pattern_count(lines: List[int], pattern: str) -> bool:
  count = 0
  for line in lines:
    if re.search(pattern, ''.join(map(str, line))):
      count += 1
  return count

def win_game(board_state: List[int], board_size: int, current_player: PlayerColor,
  latest_player: PlayerLatest, latest_action: int) -> bool:
  marked_board = utils.mark_latest(board_state, latest_action)
  marked_lines = utils.get_target_lines(marked_board, board_size, latest_action)
  return match_pattern(marked_lines, rpc.compile_go_ren(current_player, latest_player))

def inline_violation(lines: List[int], current_player: PlayerColor,
  latest_player: PlayerLatest) -> RulePattern:
  violation_patterns = {
    RulePattern.TYO_REN: rpc.compile_tyo_ren(current_player, latest_player),
    RulePattern.YONYON_RYOTO: rpc.compile_yonyon_ryoto(current_player, latest_player),
    RulePattern.YONYON_TYODA: rpc.compile_yonyon_tyoda(current_player, latest_player),
    RulePattern.YONYON_SORYU: rpc.compile_yonyon_soryu(current_player, latest_player)
  }
  for pattern, regix in violation_patterns.items():
    if match_pattern(lines, regix):
      return pattern
  return RulePattern.NONE

def multi_line_violation(lines: List[int], current_player: PlayerColor,
  latest_player: PlayerLatest) -> RulePattern:
  violation_patterns = {
    RulePattern.SANSAN: rpc.compile_san(current_player, latest_player),
    RulePattern.YONYON: rpc.compile_yon(current_player, latest_player)
  }
  for pattern, regix in violation_patterns.items():
    if match_pattern_count(lines, regix) > 1:
      return pattern
  return RulePattern.NONE

def lose_game(board_state: List[int], board_size: int, current_player: PlayerColor,
  latest_player: PlayerLatest, latest_action: int) -> bool:
  marked_board = utils.mark_latest(board_state, latest_action)
  marked_lines = utils.get_target_lines(marked_board, board_size, latest_action)

  inline_result = inline_violation(marked_lines, current_player, latest_player)
  if inline_result is not RulePattern.NONE:
    inline_result.print_result(current_player)
    return True

  multi_line_result = multi_line_violation(marked_lines, current_player, latest_player)
  if multi_line_result is not RulePattern.NONE:
    multi_line_result.print_result(current_player)
    return True

  return False

def judge_game(board_state: List[int], board_size: int, current_player: PlayerColor,
  latest_player: PlayerLatest, latest_action: int) -> int:
  if win_game(board_state, board_size, current_player, latest_action):
    return 1
  elif lose_game(board_state, board_size, current_player, latest_player, latest_action):
    return -1
  else:
    return 0

def legal_actions(board_state: List[int]) -> List[int]:
  '''
  Return list of legal actions based on the board state and current player color.
  Contains actions resulted in lose because of against of the rule.
  '''
  legal = lambda s: s[1] is PlayerColor.EMPTY
  action = lambda s: s[0]
  return list(map(action, filter(legal, enumerate(board_state))))

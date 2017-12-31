# -*- coding:utf-8 -*-

'''
Utility module for renju envs.
@auther: Arata Kokubun
@data: 2017/12/09
'''

# Imports
from typing import List, Tuple
import copy

from gym_renju.envs.core.domain.player import PlayerColor, PlayerLatest
from gym_renju.envs.core.domain.rule_pattern import RulePattern
from gym_renju.envs.core.domain.result import Result

def valid_player_colors() -> List[PlayerColor]:
  return [PlayerColor.BLACK, PlayerColor.WHITE]

def next_player(current_player: PlayerColor) -> PlayerColor:
  assert current_player in valid_player_colors()
  if current_player is PlayerColor.BLACK:
    return PlayerColor.WHITE
  elif current_player is PlayerColor.WHITE:
    return PlayerColor.BLACK

def index_to_coords(index: int, board_size: int) -> Tuple:
  return (int(index/board_size), index%board_size)

def coords_to_index(coords: Tuple, board_size: int) -> int:
  return coords[0]*board_size + coords[1]

def get_target_lines(board_state: List[int], board_size: int,
  latest_action: int) -> Tuple[List[int], List[int]]:
  coords = index_to_coords(latest_action, board_size)

  rb_start = (coords[0] - min(coords[0], coords[1]), coords[1] - min(coords[0], coords[1]))
  rb_start_index = coords_to_index(rb_start, board_size)
  rb_end_index = board_size**2 if rb_start[0] > 0 else board_size * (board_size - rb_start[1])

  col_from_right = board_size - 1 - coords[1]
  lb_start = (coords[0] - min(coords[0], col_from_right),
    coords[1] + min(coords[0], col_from_right))
  lb_start_index = coords_to_index(lb_start, board_size)
  lb_end_index = board_size**2 - 1 \
    if lb_start[0] > 0 else board_size * (lb_start[1] + 1) - 1

  return [
    board_state[coords[0]*board_size:(coords[0]+1)*board_size],
    board_state[coords[1]::board_size],
    board_state[rb_start_index:rb_end_index:board_size+1],
    board_state[lb_start_index:lb_end_index:board_size-1],
  ]

def color_to_latest(current_player_index: int) -> PlayerLatest:
  current_player = PlayerColor(current_player_index)
  assert current_player in valid_player_colors()
  if current_player is PlayerColor.BLACK:
    return PlayerLatest.BLACK
  elif current_player is PlayerColor.WHITE:
    return PlayerLatest.WHITE

def mark_latest(board_state: List[int], latest_action: int) -> List[int]:
  current_color = board_state[latest_action]
  latest_color = color_to_latest(current_color)
  copied_board = copy.deepcopy(board_state)
  copied_board[latest_action] = latest_color.value
  return copied_board

def board_full(board_state: List[int]) -> bool:
  return all(s is not PlayerColor.EMPTY.value for s in board_state)

WIN_PATTERN = [RulePattern.GO_REN]
LOSE_PATTERN = [
  RulePattern.TYO_REN, RulePattern.YONYON_RYOTO, RulePattern.YONYON_TYODA,
  RulePattern.YONYON_SORYU, RulePattern.YONYON, RulePattern.SANSAN]
DRAW_PATTERN = [
  RulePattern.FULL
]
def pattern_to_result(pattern: RulePattern) -> Result:
  if pattern in WIN_PATTERN:
    return Result.WIN
  elif pattern in LOSE_PATTERN:
    return Result.LOSE
  elif pattern in DRAW_PATTERN:
    return Result.DRAW
  else:
    return Result.NONE

def finish(result: Result) -> bool:
  return result in [Result.WIN, Result.LOSE, Result.DRAW]

SYMBOL_MAP = {
  PlayerColor.EMPTY: '.',
  PlayerColor.BLACK: 'X',
  PlayerColor.WHITE: 'O',
}
def color_to_symbol(current_player_index: int) -> str:
  return SYMBOL_MAP.get(PlayerColor(current_player_index))

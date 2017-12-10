# -*- coding:utf-8 -*-

'''
Utility module for renju envs.
@auther: Arata Kokubun
@data: 2017/12/09
'''

# Imports
from typing import List, Tuple
from gym_renju.envs.player import PlayerColor
from gym_renju.envs.utils.invalid_type_exception import InvalidPlayerColorException as IpcException

def next_player(current_player: PlayerColor) -> PlayerColor:
  if current_player is PlayerColor.BLACK:
    return PlayerColor.WHITE
  elif current_player is PlayerColor.WHITE:
    return PlayerColor.BLACK
  else:
    raise IpcException(current_player)

def valid_player_colors() -> List[PlayerColor]:
  return [PlayerColor.BLACK, PlayerColor.WHITE]

def index_to_coords(index: int, board_size: int) -> Tuple:
  return (int(index/board_size), index%board_size)

def coords_to_index(coords: Tuple, board_size: int) -> int:
  return coords[0]*board_size + coords[1]

def get_target_lines(board_state: List[int], board_size: int, latest_action: int) -> List[List[int]]:
  coords = index_to_coords(latest_action, board_size)
  right_below_start = coords_to_index((coords[0] - min(coords[0], coords[1]),
    coords[1] - min(coords[0], coords[1])), board_size)
  col_from_right = board_size - 1 - coords[1]
  left_below_start = coords_to_index((coords[0] - min(coords[0], col_from_right),
    coords[1] + min(coords[0], col_from_right)), board_size)
  return [
    board_state[coords[0]*board_size:(coords[0]+1)*board_size],
    board_state[coords[1]::board_size],
    board_state[right_below_start::board_size+1],
    board_state[left_below_start::board_size-1]
  ]

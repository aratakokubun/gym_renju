# -*- coding:utf-8 -*-

'''
Rule definition modules for Renju Game .
@auther: Arata Kokubun
@data: 2017/12/04
'''

from typing import List, Tuple
import operator

from gym_renju.envs.core.domain.player import PlayerColor
from gym_renju.envs.core.domain.rule_pattern import RulePattern
from gym_renju.envs.core.contract.factory import RuleMatcherFactory
from gym_renju.envs.utils import utils

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

def judge_game(factory: RuleMatcherFactory, board_state: List[int], board_size: int,
  current_player: PlayerColor, latest_action: int) -> RulePattern:
  marked_board = utils.mark_latest(board_state, latest_action)
  marked_lines = utils.get_target_lines(marked_board, board_size, latest_action)
  rule_matchers = factory.generate(current_player)
  for matcher in rule_matchers:
    if matcher.match(marked_lines):
      return matcher.get_rule_pattern()
  if utils.board_full(board_state):
    return RulePattern.FULL
  return RulePattern.NONE

def legal_actions(board_state: List[int]) -> List[int]:
  '''
  Return list of legal actions based on the board state and current player color.
  Contains actions resulted in lose because of against of the rule.
  '''
  legal = lambda s: s[1] == PlayerColor.EMPTY.value
  action = lambda s: s[0]
  return list(map(action, filter(legal, enumerate(board_state))))

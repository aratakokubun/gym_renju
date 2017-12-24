# -*- coding:utf-8 -*-

'''
Renju Game Gyn Environment.
@auther: Arata Kokubun
@data: 2017/12/04
'''

# Imports
from typing import List, Tuple
import sys
import numpy as np
import gym
from gym import spaces
from gym import error
from gym.utils import seeding
from six import StringIO

from gym_renju.envs.core.domain.player import PlayerType, PlayerColor
from gym_renju.envs.core.domain.result import Result
from gym_renju.envs.core.contract.container import Container
from gym_renju.envs.renju import RenjuState, RenjuBoard
from gym_renju.envs.rule import rule
from gym_renju.envs.utils import utils
from gym_renju.envs import renju_container

class RenjuEnv(gym.Env):
  metadata = {"render.modes": ["human", "ansi"]}

  def __init__(self, players: List, board_size: int = 9, swap_first: bool = False) -> None:
    '''
    @param players: List of player types
    @param board_size: board size
    '''
    # Compile DI container
    self._container = renju_container.compile_container()

    self._players = list(map(lambda player: self._container.get_policy_factory().generate(player), players))
    self._board_size = board_size
    self._board = RenjuBoard(board_size)
    self._swap_first = swap_first

    # Set env attributes
    shape = (board_size, board_size)
    self.observation_space = spaces.Box(np.zeros(shape), np.ones(shape))
    self.action_space = self._container.get_space_factory().generate(board_size**2)
    # Not effective to set reward limit
    # self.reward_range = (-100, 100)

    # Set attributes to keep states
    self._reset()

  def _reset(self) -> None:
    self._state = RenjuState(RenjuBoard(self._board_size), PlayerColor.BLACK)
    self._states = [self._state]
    self._actions = []
    self.action_space = self._container.get_space_factory().generate(self._board_size**2)
    self._start()

  def _start(self) -> None:
    # TODO: Start game
    pass

  def _seed(self, seed=None) -> List:
      seed1 = seeding.np_random(seed)
      # Derive a random seed.
      seed2 = seeding.hash_seed(seed1 + 1) % 2**32
      return [seed1, seed2]

  def _render(self, mode="human", close=False) -> StringIO:
    if close:
      return
    outfile = StringIO() if mode == 'ansi' else sys.stdout
    outfile.write(repr(self._state) + '\n')
    return outfile

  def _sar(self, action: int) -> Tuple:
    pattern = rule.judge_game(self._container.get_rule_matcher_factory(),
      self._state.get_board().get_board_state(), self._board_size,
      self._state.get_player_color(), action)
    result = utils.pattern_to_result(pattern)
    if utils.board_full()
    if result is Result.WIN:
      return self._state.get_board(), 1, True, {'state': self._state.get_board()}
    elif result is Result.WIN:
      return self._state.get_board(), -1, True, {'state': self._state.get_board()}
    elif result is Result.DRAW:
      return self._state.get_board(), 0., True, {'state': self._state.get_board()}
    else:
      # FIXME: Play Auto player
      return self._state.get_board(), 0., False, {'state': self._state.get_board()}

  def _step(self, action: int) -> Tuple:
    '''
        Returns:
            observation (object): agent's observation of the current environment
            reward (float) : amount of reward returned after previous action
            done (boolean): whether the episode has ended, in which case further step() calls will return undefined results
            info (dict): contains auxiliary diagnostic information (helpful for debugging, and sometimes learning)
    '''
    if self.action_space.contains(action):
      raise error.Error('Action[{}] is not in space'.format(action))

    self._state = self._state.act(action)
    self._actions.append(self._state.get_board().get_last_action())
    self.action_space.remove(action) # remove current action from action_space

    # FIXME: Refactor
    pattern = rule.judge_game(self._container.get_rule_matcher_factory(),
      self._state.get_board().get_board_state(), self._board_size,
      self._state.get_player_color(), action)
    result = utils.pattern_to_result(pattern)
    if result is Result.WIN:
      return self._state.get_board(), 1, True, {'state': self._state.get_board()}
    elif result is Result.WIN:
      return self._state.get_board(), -1, True, {'state': self._state.get_board()}
    elif result is Result.DRAW:
      return self._state.get_board(), 0., True, {'state': self._state.get_board()}
    else:
      # FIXME: Play Auto player
      return self._state.get_board(), 0., False, {'state': self._state.get_board()}

  def get_state(self) -> RenjuState:
    return self._state

  def get_actions(self) -> List[int]:
    return self._actions

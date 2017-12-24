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

from gym_renju.envs.core.domain.player import PlayerColor
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

    policy_factory = self._container.get_policy_factory()
    self._policies = {
      PlayerColor.BLACK: policy_factory.generate(players[0]),
      PlayerColor.WHITE: policy_factory.generate(players[1])
    }
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

  def _step_auto(self):
    next_player = utils.next_player(self._state.get_player_color())
    policy = self._policies.get(next_player)
    if policy.auto_act():
      # Calling _step recursively but not calling it more than 2 times.
      # So this is not problematic for recursive calling.
      action = policy.act(self._state.get_board().get_board_state(), self.action_space, next_player)
      self._step(action)

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

    board = self._state.get_board()
    pattern = rule.judge_game(self._container.get_rule_matcher_factory(), board.get_board_state(),
      self._board_size, self._state.get_player_color(), action)
    result = utils.pattern_to_result(pattern)
    reward = self._container.get_reward_factory().generate().get_reward(result)
    if utils.finish(result):
      return board, reward, True, {'state': board}
    else:
      self._step_auto()
      return board, reward, True, {'state': board}

  def get_state(self) -> RenjuState:
    return self._state

  def get_actions(self) -> List[int]:
    return self._actions

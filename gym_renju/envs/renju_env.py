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
from gym_renju.envs.core.domain.rule_pattern import RulePattern
from gym_renju.envs.core.domain.result import Result
from gym_renju.envs.renju import RenjuState, RenjuBoard
from gym_renju.envs.rule import rule
from gym_renju.envs.utils import utils
from gym_renju.envs import renju_container
from gym_renju.envs.renju_container import RenjuContainer

class RenjuEnv(gym.Env):
  metadata = {"render.modes": ["human", "ansi"]}
  default_container = renju_container.compile_container()

  def __init__(self, players: List, board_size: int = 9, swap_first: bool = False,
    container: RenjuContainer = default_container) -> None:
    '''
    @param players: List of player types
    @param board_size: board size
    '''
    self._container = container
    policy_factory = self._container.get_policy_factory()
    self._policies = {
      PlayerColor.BLACK: policy_factory.generate(players[0]),
      PlayerColor.WHITE: policy_factory.generate(players[1])
    }
    self._board_size = board_size
    self._swap_first = swap_first

    # Set env attributes
    shape = (board_size, board_size)
    self.observation_space = spaces.Box(np.zeros(shape), np.ones(shape))
    self.action_space = self._container.get_space_factory().generate(board_size**2)
    # Not effective to set reward limit
    # self.reward_range = (-100, 100)

    # Set attributes to keep states
    self._state = RenjuState(RenjuBoard(self._board_size), PlayerColor.WHITE, PlayerColor.BLACK)
    self._states = [self._state]
    self._actions = []
    self._latest_rule_pattern = RulePattern.NONE
    self._step_auto()

  def _step_auto(self) -> None:
    next_player = self._state.get_next_player()
    policy = self._policies.get(next_player)
    if policy.auto_act():
      # Calling _step recursively but not calling it more than 2 times.
      # So this is not problematic for recursive calling.
      action = policy.act(self._state.get_board().get_board_state(), self.action_space, next_player)
      self._step(action)

  def _reset(self) -> List:
    if self._swap_first:
      self._policies[PlayerColor.BLACK], self._policies[PlayerColor.WHITE] = \
        self._policies[PlayerColor.WHITE], self._policies[PlayerColor.BLACK]
    self._state = RenjuState(RenjuBoard(self._board_size), PlayerColor.WHITE, PlayerColor.BLACK)
    self._states = [self._state]
    self._actions = []
    self._latest_rule_pattern = RulePattern.NONE
    self.action_space = self._container.get_space_factory().generate(self._board_size**2)
    self._step_auto()
    return self._state.get_board().to_np_arr()

  def _seed(self, seed=None) -> List:
      seed1 = seeding.np_random(seed)
      # Derive a random seed.
      seed2 = seeding.hash_seed(seed1 + 1) % 2**32
      return [seed1, seed2]

  def _render(self, mode="human", close=False) -> StringIO:
    if close:
      return
    outfile = StringIO() if mode == 'ansi' else sys.stdout
    latest_result = utils.pattern_to_result(self._latest_rule_pattern)
    if utils.finish(latest_result):
      outfile.write(self._repr_result(latest_result) + '\n')
    outfile.write(repr(self._state) + '\n')
    return outfile

  def _repr_result(self, result: Result) -> str:
    latest_player = self._state.get_latest_player()
    latest_action = self._state.get_board().get_last_action()
    out = 'Game end on {0}\'s tern with {1}: last move: {2}\n'\
      .format(latest_player.name, self._latest_rule_pattern.name, latest_action)
    if result is Result.WIN:
      out += 'Player {0} Wins!'.format(latest_player.name)
    elif result is Result.LOSE:
      opponent = self._state.get_next_player()
      out += 'Player {0} Wins!'.format(opponent.name)
    else:
      out += 'Draw game!'
    return out

  def _step(self, action: int) -> Tuple:
    '''
        Returns:
            observation (object): agent's observation of the current environment
            reward (float) : amount of reward returned after previous action
            done (boolean): whether the episode has ended, in which case further step() calls will return undefined results
            info (dict): contains auxiliary diagnostic information (helpful for debugging, and sometimes learning)
    '''
    if not self.action_space.contains(action):
      raise error.Error('Action[{}] is not in space'.format(action))
    
    if utils.finish(utils.pattern_to_result(self._latest_rule_pattern)):
      raise error.Error('Game already finished. Get rewards with "get_rewards_afeter_game" and then "reset" the env.')

    next_player = self._state.get_next_player()
    self._state = self._state.act(action)
    self._actions.append(self._state.get_board().get_last_action())
    self.action_space.remove(action) # remove current action from action_space

    board = self._state.get_board()
    self._latest_rule_pattern = rule.judge_game(self._container.get_rule_matcher_factory(), board.get_board_state(),
      self._board_size, next_player, action)
    result = utils.pattern_to_result(self._latest_rule_pattern)
    if utils.finish(result):
      reward = self._container.get_reward_factory().generate().get_reward(next_player, result)
      return board.to_np_arr(), reward, True, {'state': board}
    else:
      self._step_auto()
      result = utils.pattern_to_result(self._latest_rule_pattern)
      reward = self._container.get_reward_factory().generate().get_opponent_reward(next_player, result)
      return self._state.get_board().to_np_arr(), reward, utils.finish(result), {'state': self._state}

  def get_state(self) -> RenjuState:
    return self._state

  def get_actions(self) -> List[int]:
    return self._actions

  def get_rewards(self) -> List[float]:
    '''
    Get rewards of both players.
    @return List of rewards, with [0]:<BLACK:Reward of player first> [1]:<WHITE:Reward of draw first>
    '''
    result = utils.pattern_to_result(self._latest_rule_pattern)
    last_player = self._state.get_latest_player()
    next_player = self._state.get_next_player()
    last_player_reward = self._container.get_reward_factory().generate().get_reward(
      last_player, result)
    next_player_reward = self._container.get_reward_factory().generate().get_opponent_reward(
      next_player, result)
    if last_player is PlayerColor.BLACK:
      return [last_player_reward, next_player_reward]
    else:
      return [next_player_reward, last_player_reward]

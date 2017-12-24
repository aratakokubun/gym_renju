# -*- coding:utf-8 -*-

'''
Reward module for Renju.
@auther: Arata Kokubun
@date: 2017/12/23
'''

# Imports
import json

from gym_renju.envs.core.domain.result import Result
from gym_renju.envs.core.domain.player import PlayerColor
from gym_renju.envs.core.contract.reward import Reward

class ConfiguredReward(Reward):
  '''
  Defined reward from configuration file
  '''

  def __init__(self, path: str = 'gym_renju/data/reward.json'):
    '''
    @param path: file path to read from configuration
    @throws JSONDecodeError on failed to read json
    '''
    data = json.load(open(path))
    self._reward_map = {}
    self._reward_map[PlayerColor.BLACK] = {}
    self._reward_map[PlayerColor.WHITE] = {}
    self._reward_map[PlayerColor.BLACK][Result.WIN] = data["win"]
    self._reward_map[PlayerColor.BLACK][Result.LOSE] = data["lose"]
    self._reward_map[PlayerColor.BLACK][Result.DRAW] = data["draw"]["playFirst"]
    self._reward_map[PlayerColor.BLACK][Result.NONE] = data["other"]
    self._reward_map[PlayerColor.WHITE][Result.WIN] = data["win"]
    self._reward_map[PlayerColor.WHITE][Result.LOSE] = data["lose"]
    self._reward_map[PlayerColor.WHITE][Result.DRAW] = data["draw"]["drawFirst"]
    self._reward_map[PlayerColor.WHITE][Result.NONE] = data["other"]

  def get_reward(self, player: PlayerColor, result: Result) -> float:
    return self._reward_map[player][result]

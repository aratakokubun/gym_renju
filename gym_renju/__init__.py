from gym.envs.registration import register

# Environment for human vs ai with basic level
register(
    id='Renju19x19-v0',
    entry_point='gym_renju.envs:RenjuEnv',
    kwargs={
        'player_black': 'input',
        'player_white': 'begginer',
        'board_size': 19,
    },
    nondeterministic=True,
)

# Environment for machine learning.
# Can act both black and white
register(
    id='Renju19x19-learning-v0',
    entry_point='gym_renju.envs:RenjuEnv',
    kwargs={
        'player_black': 'input',
        'player_white': 'input',
        'board_size': 19,
        'swap_first': True,
        'rule': 'RIF'
    },
    nondeterministic=True,
)

# TODO: Add more envs to player game with different type of AI
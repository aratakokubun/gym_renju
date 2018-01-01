from gym.envs.registration import register

# Environment for human vs ai with basic level
register(
    id='Renju15x15-v0',
    entry_point='gym_renju.envs:RenjuEnv',
    kwargs={
        'players': ['input', 'random'],
        'board_size': 15,
        'swap_first': True,
    },
    nondeterministic=True,
)

# Environment for machine learning.
# Can act both black and white
register(
    id='Renju15x15-learning-v0',
    entry_point='gym_renju.envs:RenjuEnv',
    kwargs={
        'players': ['input', 'input'],
        'board_size': 15,
        'swap_first': True,
    },
    nondeterministic=True,
)

register(
    id='Renju15x15-learning-noswap-v0',
    entry_point='gym_renju.envs:RenjuEnv',
    kwargs={
        'players': ['input', 'input'],
        'board_size': 15,
        'swap_first': False,
    },
    nondeterministic=True,
)

# TODO: Add more envs to player game with different type of AI
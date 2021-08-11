from gym.envs.registration import register

register(
    id='sheep_env-v0',                                   # Format should be xxx-v0, xxx-v1....
    entry_point='sheep_gym.envs:SheepEnv',              # Expalined in envs/__init__.py
)
register(
    id='sheep_env_extend-v0',
    entry_point='sheep_gym.envs:SheepEnvExtend',
)

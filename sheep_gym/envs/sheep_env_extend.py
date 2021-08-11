import gym

class SheepEnvExtend(gym.Env):
    def __init__(self):
        print('SheepEnvExtend Environment initialized')
    def step(self):
        print('SheepEnvExtend Step successful!')
    def reset(self):
        print('SheepEnvExtend Environment reset')

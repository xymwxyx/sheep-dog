import gym

class SheepEnv(gym.Env):
    def __init__(self):
        print('SheepEnv Environment initialized')
    def step(self):
        print('SheepEnv Step successful!')
    def reset(self):
        print('SheepEnv Environment reset')

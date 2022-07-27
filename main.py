import time
import gym
import gym_minigrid
import numpy as np

### actions available
def actions_available(i):
	if i%3==0:
		return env.actions.left
	elif i%3==1:
		return env.actions.right
	elif i%3==2:
		return env.actions.forward

### random player
class Player():

    def play_random(obs):
        action=actions_available(np.random.choice(3))
        return action

### play multiple games
def multiple_games(n_games, max_steps):
    for i in range(n_games):
        obs=env.reset()
        for j in range(max_steps):
            action=Player.play_random(obs)
            obs, reward, done, _ = env.step(action)
            env.render()
            time.sleep(0.5)
            if done:
                time.sleep(5)
                break
#=====================================================
#=====================================================
#=====================================================
env = gym.make('MiniGrid-T-16x16-v0')
multiple_games(2,10)
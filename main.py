import gym
import time
EPISODES = 1000
STEPS = 100

env = gym.make('CartPole-v0')
#env = gym.make('Asteroids-v4')

for episode in range(EPISODES):
    observation = env.reset()
    for step in range(STEPS):
        env.render()
        #observation congruent with env
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        time.sleep(0.5)

        if done:
            print("Episode {} finished after {} timesteps".format(episode, step+1))
            break

def env_info(env):
    print("Action space: {}, Type: {}".format(env.action_space, type(env.action_space)))
    print("Observation space: {}, Type: {}".format(env.observation_space, type(env.action_space)))
    print("Reward range: {}, Type: {}".format(env.reward_range, type(env.reward_range)))


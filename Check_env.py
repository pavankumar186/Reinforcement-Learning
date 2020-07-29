import gym
env=gym.make("MountainCar-v0")
print("The number of possible actions we can take are {}".format(env.action_space))
#Outputs Discrete(3) which means that the possible actions 
#are discrete and are 0,1 and 2
print("The number of observation variables we have are {}".format(env.observation_space))
#Outputs Box(2,) which means we have 2 variables that we can observe
#also to find the limits of these variables we do the following
print(env.observation_space.high)
print(env.observation_space.low)

env.reset()
for i in range(100):
	new_state,reward,done,info=env.step(env.action_space.sample())
	env.render()
env.close()

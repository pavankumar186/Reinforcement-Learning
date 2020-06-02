import gym
import numpy as np
env=gym.make("MountainCar-v0")
env.reset()
LR=0.1
Discount=0.9

Dis_os_size=[20,20]
dis_os_step_size=(env.observation_space.high-env.observation_space.low)/[20,20]
# print(dis_os_step_size)
qtab=np.random.uniform(low=-2,high=0,size=[20,20,3])
# print(qtab)
def get_discrete(new):
	dis_new=(new-env.observation_space.low)/dis_os_step_size
	return tuple(dis_new.astype(np.int))
dis_new=get_discrete(env.reset())

print(dis_new,env.reset())
print(np.argmax(qtab[dis_new]))
# '''


for i in range(5000):
	done=False
	dis_current=get_discrete(env.reset())
	while not done:

		action=np.argmax(qtab[dis_current])
		new,rew,done,info=env.step(action)
		# print(new,rew,done,info)
		dis_new=get_discrete(new)
		if i%200==0:
			# print(new,rew,info)
			env.render()
		if not done:
			max_future_q=np.max(qtab[dis_new])
			curr_q=qtab[dis_current+(action,)]
			# print(curr_q)
			qtab[dis_current+(action,)]=(1-LR)*curr_q + LR*(rew+Discount*max_future_q)
		elif new[0]>=env.goal_position:
			print("Reached at {}".format(i))
			qtab[dis_current+(action,)]=0
		dis_current=dis_new
env.close()
#'''
import time
import gym
import numpy as np
env=gym.make("CartPole-v1")
# print(env.observation_space.low)
# print(env.observation_space.high)
def getdis(new):
	step=int(new[0])
	if new[1]!=0:
		step_v=int(abs(new[1])/(new[1]))
	else:
		step_v=0
	angle=int(new[2]*45*7/22)
	if new[3]!=0:
		angle_v=int(abs(new[3])/(new[3]))
	else:
		angle_v=0
	return (angle,angle_v)
# a=getdis(env.reset())
# print(a)
LR=0.1
Discount=1
Episodes=1000

size=[12,3,2]
qtab=np.random.uniform(low=0,high=1,size=size)

for i in range(Episodes):
	cur=env.reset()
	discur=getdis(env.reset())
	done=False
	score=0
	while not done:
		action=np.argmax(qtab[discur])
		new,rew,done,info=env.step(action)
		disnew=getdis(new)
		if i%5000==0:
			env.render()
			time.sleep(0.05)
		if not done:
			max_fut=max(qtab[disnew])
			cur_q=qtab[discur+(action,)]
			qtab[discur+(action,)]=(1-LR)*cur_q + LR*(rew+ max_fut)
			score+=1
		discur=disnew
		cur=new
	if score>190:
		print(score,i)
env.close()

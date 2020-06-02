import time
import gym
import numpy as np
env=gym.make("CartPole-v1")
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
LR=0.7
Discount=1
Epsilon=0.5
Episodes=1000
LR_decay=LR/(Episodes//2)
Epsilon_decay=Epsilon/(Episodes//2)
size=[12,3,2]
qtab=np.random.uniform(low=0,high=0,size=size)
# olsc=20
avg_rew=0
for i in range(Episodes):
	tot_rew=0
	cur=env.reset()
	discur=getdis(cur)
	done=False
	while not done:
		if np.random.random()>Epsilon:
			action=np.argmax(qtab[discur])
		else:
			action=np.random.randint(0,env.action_space.n)
		new,rew,done,info=env.step(action)
		tot_rew+=rew
		disnew=getdis(new)
		# if i%1000==0:
			# env.render()
# 			time.sleep(0.05)
		if not done:
			max_fut=max(qtab[disnew])
			cur_q=qtab[discur+(action,)]
			qtab[discur+(action,)]=(1-LR)*cur_q + LR*(rew+ Discount* max_fut)
		discur=disnew
		cur=new
	if Episodes//2 >= i >=1:
		Epsilon-=Epsilon_decay
		LR-=LR_decay
	# if i>=9900:
	# 	avg_rew+=tot_rew
	# if i==9999:
	# 	print(avg_rew/100)
	if tot_rew>190:
		print(tot_rew)
env.close()
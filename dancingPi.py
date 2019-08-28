#!/usr/bin/env python3
# File name   : dancingPi.py
# Author	  : William
# Date		: 2019/08/27
import socket
import time
import threading
import Adafruit_PCA9685

class Servo_ctrl(threading.Thread):
	def __init__(self, *args, **kwargs):
		super(Servo_ctrl, self).__init__(*args, **kwargs)
		self.__flag = threading.Event()
		self.__flag.set()
		self.__running = threading.Event()
		self.__running.set()

	def run(self):
		global goal_pos, servo_command, init_get, if_continue, walk_step
		while self.__running.isSet():
			self.__flag.wait()
			if function_select == 'B':
				if_continue = move_smooth(position_select)
				send_all_pwm()
			elif function_select == 'D':
				if_continue = move_config(position_select)
				send_all_pwm()

			while function_select == 'E':
				walk(walk_step)
				walk_step += 1
				if walk_step == 9:
					walk_step = 1
			else:
				servos.pause()

			print('loop')
			if if_continue:
				continue
			else:
				servos.pause()

	def pause(self):
		self.__flag.clear()

	def resume(self):
		self.__flag.set()

	def stop(self):
		self.__flag.set()
		self.__running.clear()


def old_update():
	global old_pwm
	old_pwm = []
	old_pwm.append(PWM_0)
	old_pwm.append(PWM_1)
	old_pwm.append(PWM_2)
	old_pwm.append(PWM_3)
	old_pwm.append(PWM_4)
	old_pwm.append(PWM_5)
	old_pwm.append(PWM_6)
	old_pwm.append(PWM_7)
	old_pwm.append(PWM_8)
	old_pwm.append(PWM_9)
	old_pwm.append(PWM_10)
	old_pwm.append(PWM_11)
	old_pwm.append(PWM_12)
	old_pwm.append(PWM_13)
	old_pwm.append(PWM_14)
	old_pwm.append(PWM_15)   #Add PWM value to old_pwm

def init_servos():
	global PWM_0, PWM_1, PWM_2, PWM_3, PWM_4, PWM_5, PWM_6, PWM_7, PWM_8, PWM_9, PWM_10, PWM_11, PWM_12, PWM_13, PWM_14, PWM_15
	pwm.set_pwm(0,0,S0_init)
	pwm.set_pwm(1,0,S1_init)
	pwm.set_pwm(2,0,S2_init)
	pwm.set_pwm(3,0,S3_init)
	pwm.set_pwm(4,0,S4_init)
	pwm.set_pwm(5,0,S5_init)
	pwm.set_pwm(6,0,S6_init)
	pwm.set_pwm(7,0,S7_init)
	pwm.set_pwm(8,0,S8_init)
	pwm.set_pwm(9,0,S9_init)
	pwm.set_pwm(10,0,S10_init)
	pwm.set_pwm(11,0,S11_init)
	pwm.set_pwm(12,0,S12_init)
	pwm.set_pwm(13,0,S13_init)
	pwm.set_pwm(14,0,S14_init)
	pwm.set_pwm(15,0,S15_init)

	PWM_0 = S0_init
	PWM_1 = S1_init
	PWM_2 = S2_init
	PWM_3 = S3_init
	PWM_4 = S4_init
	PWM_5 = S5_init
	PWM_6 = S6_init
	PWM_7 = S7_init
	PWM_8 = S8_init
	PWM_9 = S9_init
	PWM_10 = S10_init
	PWM_11 = S11_init
	PWM_12 = S12_init
	PWM_13 = S13_init
	PWM_14 = S14_init
	PWM_15 = S15_init
	old_update()

def servos_to_pwm():
	global goal_now, PWM_0, PWM_1, PWM_2, PWM_3, PWM_4, PWM_5, PWM_6, PWM_7, PWM_8, PWM_9, PWM_10, PWM_11, PWM_12, PWM_13, PWM_14, PWM_15
	goal_to_import = goal_import(position_select)
	#goal_now = goal_to_import.split()
	goal_now = goal_to_import
	PWM_0 = int(goal_now[1])
	PWM_1 = int(goal_now[2])
	PWM_2 = int(goal_now[3])
	PWM_3 = int(goal_now[4])
	PWM_4 = int(goal_now[5])
	PWM_5 = int(goal_now[6])
	PWM_6 = int(goal_now[7])
	PWM_7 = int(goal_now[8])
	PWM_8 = int(goal_now[9])
	PWM_9 = int(goal_now[10])
	PWM_10 = int(goal_now[11])
	PWM_11 = int(goal_now[12])
	PWM_12 = int(goal_now[13])
	PWM_13 = int(goal_now[14])
	PWM_14 = int(goal_now[15])
	PWM_15 = int(goal_now[16])
	
	pwm.set_pwm(0,0,PWM_0)
	pwm.set_pwm(1,0,PWM_1)
	pwm.set_pwm(2,0,PWM_2)
	pwm.set_pwm(3,0,PWM_3)
	pwm.set_pwm(4,0,PWM_4)
	pwm.set_pwm(5,0,PWM_5)
	pwm.set_pwm(6,0,PWM_6)
	pwm.set_pwm(7,0,PWM_7)
	pwm.set_pwm(8,0,PWM_8)
	pwm.set_pwm(9,0,PWM_9)
	pwm.set_pwm(10,0,PWM_10)
	pwm.set_pwm(11,0,PWM_11)
	pwm.set_pwm(12,0,PWM_12)
	pwm.set_pwm(13,0,PWM_13)
	pwm.set_pwm(14,0,PWM_14)
	pwm.set_pwm(15,0,PWM_15)
	old_update()

def servos_to_pos(pos_input):
	global PWM_0, PWM_1, PWM_2, PWM_3, PWM_4, PWM_5, PWM_6, PWM_7, PWM_8, PWM_9, PWM_10, PWM_11, PWM_12, PWM_13, PWM_14, PWM_15
	PWM_0 = int(pos_input[1])
	PWM_1 = int(pos_input[2])
	PWM_2 = int(pos_input[3])
	PWM_3 = int(pos_input[4])
	PWM_4 = int(pos_input[5])
	PWM_5 = int(pos_input[6])
	PWM_6 = int(pos_input[7])
	PWM_7 = int(pos_input[8])
	PWM_8 = int(pos_input[9])
	PWM_9 = int(pos_input[10])
	PWM_10 = int(pos_input[11])
	PWM_11 = int(pos_input[12])
	PWM_12 = int(pos_input[13])
	PWM_13 = int(pos_input[14])
	PWM_14 = int(pos_input[15])
	PWM_15 = int(pos_input[16])
	
	pwm.set_pwm(0,0,PWM_0)
	pwm.set_pwm(1,0,PWM_1)
	pwm.set_pwm(2,0,PWM_2)
	pwm.set_pwm(3,0,PWM_3)
	pwm.set_pwm(4,0,PWM_4)
	pwm.set_pwm(5,0,PWM_5)
	pwm.set_pwm(6,0,PWM_6)
	pwm.set_pwm(7,0,PWM_7)
	pwm.set_pwm(8,0,PWM_8)
	pwm.set_pwm(9,0,PWM_9)
	pwm.set_pwm(10,0,PWM_10)
	pwm.set_pwm(11,0,PWM_11)
	pwm.set_pwm(12,0,PWM_12)
	pwm.set_pwm(13,0,PWM_13)
	pwm.set_pwm(14,0,PWM_14)
	pwm.set_pwm(15,0,PWM_15)
	old_update()

def num_import_int(initial):		#Call this function to import data from '.txt' file
	global r
	with open("config.txt") as f:
		for line in f.readlines():
			if(line.find(initial) == 0):
				r=line
	begin=len(list(initial))
	snum=r[begin:]
	n=int(snum)
	return n

def goal_import(initial):		#Call this function to import data from '.txt' file
	global r
	with open("config.txt") as f:
		for line in f.readlines():
			if(line.find(initial) == 0):
				r=line
	begin=len(list(initial))
	snum=r[begin:]
	snum = snum.split()
	return snum

def replace_num(initial,new_num):   #Call this function to replace data in '.txt' file
	newline=""
	str_num=str(new_num)
	with open("config.txt","r") as f:
		for line in f.readlines():
			if(line.find(initial) == 0):
				line = initial+"%s" %(str_num+"\n")
			newline += line
	with open("config.txt","w") as f:
		f.writelines(newline)

def send_all_pwm():
	pwm_to_send ='PWM '+str(PWM_0)+' '+str(PWM_1)+' '+str(PWM_2)+' '+str(PWM_3)+' '+str(PWM_4)+' '+str(PWM_5)+' '+str(PWM_6)+' '+str(PWM_7)+' '
	pwm_to_send = pwm_to_send+str(PWM_8)+' '+str(PWM_9)+' '+str(PWM_10)+' '+str(PWM_11)+' '+str(PWM_12)+' '+str(PWM_13)+' '+str(PWM_14)+' '+str(PWM_15)
	tcpCliSock.send(pwm_to_send.encode())

def move_input():

	def move_fast():
		servos_to_pwm()
		send_all_pwm()

	if function_select == 'A':
		move_fast()
	elif function_select == 'B':
		if not if_continue:
			servos.resume()
	elif function_select == 'D':
		servos.resume()

def move_smooth_base(servo_name, goal_pwm, pwm_old, now_pos, total_range):
	pwm_input = int(pwm_old+(goal_pwm-pwm_old)*now_pos/total_range)
	pwm.set_pwm(servo_name, 0, pwm_input)
	return pwm_input

def move_smooth(position_start):
	global PWM_0, PWM_1, PWM_2, PWM_3, PWM_4, PWM_5, PWM_6, PWM_7, PWM_8, PWM_9, PWM_10, PWM_11, PWM_12, PWM_13, PWM_14, PWM_15
	goal_input = goal_import(position_start)
	for i in range(0,pix_input):
		if position_select != position_start:
			old_update()
			return 1
		PWM_0 = move_smooth_base(0, int(goal_input[1]), old_pwm[0], i, pix_input)
		PWM_1 = move_smooth_base(1, int(goal_input[2]), old_pwm[1], i, pix_input)
		PWM_2 = move_smooth_base(2, int(goal_input[3]), old_pwm[2], i, pix_input)
		PWM_3 = move_smooth_base(3, int(goal_input[4]), old_pwm[3], i, pix_input)
		PWM_4 = move_smooth_base(4, int(goal_input[5]), old_pwm[4], i, pix_input)
		PWM_5 = move_smooth_base(5, int(goal_input[6]), old_pwm[5], i, pix_input)
		PWM_6 = move_smooth_base(6, int(goal_input[7]), old_pwm[6], i, pix_input)
		PWM_7 = move_smooth_base(7, int(goal_input[8]), old_pwm[7], i, pix_input)
		PWM_8 = move_smooth_base(8, int(goal_input[9]), old_pwm[8], i, pix_input)
		PWM_9 = move_smooth_base(9, int(goal_input[10]), old_pwm[9], i, pix_input)
		PWM_10 = move_smooth_base(10, int(goal_input[11]), old_pwm[10], i, pix_input)
		PWM_11 = move_smooth_base(11, int(goal_input[12]), old_pwm[11], i, pix_input)
		PWM_12 = move_smooth_base(12, int(goal_input[13]), old_pwm[12], i, pix_input)
		PWM_13 = move_smooth_base(13, int(goal_input[14]), old_pwm[13], i, pix_input)
		PWM_14 = move_smooth_base(14, int(goal_input[15]), old_pwm[14], i, pix_input)
		PWM_15 = move_smooth_base(15, int(goal_input[16]), old_pwm[15], i, pix_input)

		time.sleep(time_input)
	PWM_0 = int(goal_input[1])
	PWM_1 = int(goal_input[2])
	PWM_2 = int(goal_input[3])
	PWM_3 = int(goal_input[4])
	PWM_4 = int(goal_input[5])
	PWM_5 = int(goal_input[6])
	PWM_6 = int(goal_input[7])
	PWM_7 = int(goal_input[8])
	PWM_8 = int(goal_input[9])
	PWM_9 = int(goal_input[10])
	PWM_10 = int(goal_input[11])
	PWM_11 = int(goal_input[12])
	PWM_12 = int(goal_input[13])
	PWM_13 = int(goal_input[14])
	PWM_14 = int(goal_input[15])
	PWM_15 = int(goal_input[16])

	pwm.set_pwm(0, 0, PWM_0)
	pwm.set_pwm(1, 0, PWM_1)
	pwm.set_pwm(2, 0, PWM_2)
	pwm.set_pwm(3, 0, PWM_3)
	pwm.set_pwm(4, 0, PWM_4)
	pwm.set_pwm(5, 0, PWM_5)
	pwm.set_pwm(6, 0, PWM_6)
	pwm.set_pwm(7, 0, PWM_7)
	pwm.set_pwm(8, 0, PWM_8)
	pwm.set_pwm(9, 0, PWM_9)
	pwm.set_pwm(10, 0, PWM_10)
	pwm.set_pwm(11, 0, PWM_11)
	pwm.set_pwm(12, 0, PWM_12)
	pwm.set_pwm(13, 0, PWM_13)
	pwm.set_pwm(14, 0, PWM_14)
	pwm.set_pwm(15, 0, PWM_15)
	old_update()
	return 0

def walk_smooth(goal_input):
	global PWM_0, PWM_1, PWM_2, PWM_3, PWM_4, PWM_5, PWM_6, PWM_7, PWM_8, PWM_9, PWM_10, PWM_11, PWM_12, PWM_13, PWM_14, PWM_15
	for i in range(0,pix_input):
		PWM_0 = move_smooth_base(0, int(goal_input[1]), old_pwm[0], i, pix_input)
		PWM_1 = move_smooth_base(1, int(goal_input[2]), old_pwm[1], i, pix_input)
		PWM_2 = move_smooth_base(2, int(goal_input[3]), old_pwm[2], i, pix_input)
		PWM_3 = move_smooth_base(3, int(goal_input[4]), old_pwm[3], i, pix_input)
		PWM_4 = move_smooth_base(4, int(goal_input[5]), old_pwm[4], i, pix_input)
		PWM_5 = move_smooth_base(5, int(goal_input[6]), old_pwm[5], i, pix_input)
		PWM_6 = move_smooth_base(6, int(goal_input[7]), old_pwm[6], i, pix_input)
		PWM_7 = move_smooth_base(7, int(goal_input[8]), old_pwm[7], i, pix_input)

		time.sleep(time_input)
	PWM_0 = int(goal_input[1])
	PWM_1 = int(goal_input[2])
	PWM_2 = int(goal_input[3])
	PWM_3 = int(goal_input[4])
	PWM_4 = int(goal_input[5])
	PWM_5 = int(goal_input[6])
	PWM_6 = int(goal_input[7])
	PWM_7 = int(goal_input[8])

	pwm.set_pwm(0, 0, PWM_0)
	pwm.set_pwm(1, 0, PWM_1)
	pwm.set_pwm(2, 0, PWM_2)
	pwm.set_pwm(3, 0, PWM_3)
	pwm.set_pwm(4, 0, PWM_4)
	pwm.set_pwm(5, 0, PWM_5)
	pwm.set_pwm(6, 0, PWM_6)
	pwm.set_pwm(7, 0, PWM_7)
	old_update()
	return 0

def move_config(position_start):
	goal_input = goal_import(position_start)
	if goal_input[0] == 'A':
		servos_to_pos(goal_input)
		time.sleep(0.2)
	elif goal_input[0] == 'B':
		global PWM_0, PWM_1, PWM_2, PWM_3, PWM_4, PWM_5, PWM_6, PWM_7, PWM_8, PWM_9, PWM_10, PWM_11, PWM_12, PWM_13, PWM_14, PWM_15
		for i in range(0,pix_input):
			PWM_0 = move_smooth_base(0, int(goal_input[1]), old_pwm[0], i, pix_input)
			PWM_1 = move_smooth_base(1, int(goal_input[2]), old_pwm[1], i, pix_input)
			PWM_2 = move_smooth_base(2, int(goal_input[3]), old_pwm[2], i, pix_input)
			PWM_3 = move_smooth_base(3, int(goal_input[4]), old_pwm[3], i, pix_input)
			PWM_4 = move_smooth_base(4, int(goal_input[5]), old_pwm[4], i, pix_input)
			PWM_5 = move_smooth_base(5, int(goal_input[6]), old_pwm[5], i, pix_input)
			PWM_6 = move_smooth_base(6, int(goal_input[7]), old_pwm[6], i, pix_input)
			PWM_7 = move_smooth_base(7, int(goal_input[8]), old_pwm[7], i, pix_input)
			PWM_8 = move_smooth_base(8, int(goal_input[9]), old_pwm[8], i, pix_input)
			PWM_9 = move_smooth_base(9, int(goal_input[10]), old_pwm[9], i, pix_input)
			PWM_10 = move_smooth_base(10, int(goal_input[11]), old_pwm[10], i, pix_input)
			PWM_11 = move_smooth_base(11, int(goal_input[12]), old_pwm[11], i, pix_input)
			PWM_12 = move_smooth_base(12, int(goal_input[13]), old_pwm[12], i, pix_input)
			PWM_13 = move_smooth_base(13, int(goal_input[14]), old_pwm[13], i, pix_input)
			PWM_14 = move_smooth_base(14, int(goal_input[15]), old_pwm[14], i, pix_input)
			PWM_15 = move_smooth_base(15, int(goal_input[16]), old_pwm[15], i, pix_input)
			time.sleep(time_input)

		PWM_0 = int(goal_input[1])
		PWM_1 = int(goal_input[2])
		PWM_2 = int(goal_input[3])
		PWM_3 = int(goal_input[4])
		PWM_4 = int(goal_input[5])
		PWM_5 = int(goal_input[6])
		PWM_6 = int(goal_input[7])
		PWM_7 = int(goal_input[8])
		PWM_8 = int(goal_input[9])
		PWM_9 = int(goal_input[10])
		PWM_10 = int(goal_input[11])
		PWM_11 = int(goal_input[12])
		PWM_12 = int(goal_input[13])
		PWM_13 = int(goal_input[14])
		PWM_14 = int(goal_input[15])
		PWM_15 = int(goal_input[16])

		pwm.set_pwm(0, 0, PWM_0)
		pwm.set_pwm(1, 0, PWM_1)
		pwm.set_pwm(2, 0, PWM_2)
		pwm.set_pwm(3, 0, PWM_3)
		pwm.set_pwm(4, 0, PWM_4)
		pwm.set_pwm(5, 0, PWM_5)
		pwm.set_pwm(6, 0, PWM_6)
		pwm.set_pwm(7, 0, PWM_7)
		pwm.set_pwm(8, 0, PWM_8)
		pwm.set_pwm(9, 0, PWM_9)
		pwm.set_pwm(10, 0, PWM_10)
		pwm.set_pwm(11, 0, PWM_11)
		pwm.set_pwm(12, 0, PWM_12)
		pwm.set_pwm(13, 0, PWM_13)
		pwm.set_pwm(14, 0, PWM_14)
		pwm.set_pwm(15, 0, PWM_15)
		old_update()
		return 0

def walk(pos):
	wiggle = 100
	height = 100
	position_walk = []
	if pos == 1:
		pwm_0 = S0_init - wiggle/2 
		pwm_1 = S1_init + height

		pwm_2 = S2_init + wiggle/2 + wiggle*2/6
		pwm_3 = S3_init + height/2

		pwm_4 = S4_init + wiggle/2
		pwm_5 = S5_init + height/2

		pwm_6 = S6_init - wiggle/2 + wiggle*2/6
		pwm_7 = S7_init - height/2
	elif pos == 2:
		pwm_0 = S0_init - wiggle/2 + wiggle*3/6
		pwm_1 = S1_init - height/2

		pwm_2 = S2_init + wiggle/2 + wiggle*1/6
		pwm_3 = S3_init + height/2

		pwm_4 = S4_init + wiggle/2 + wiggle*1/6
		pwm_5 = S5_init + height/2

		pwm_6 = S6_init - wiggle/2 + wiggle*3/6
		pwm_7 = S7_init - height/2
	elif pos == 3:
		pwm_0 = S0_init - wiggle/2 + wiggle*2/6
		pwm_1 = S1_init - height/2

		pwm_2 = S2_init + wiggle/2
		pwm_3 = S3_init + height/2

		pwm_4 = S4_init + wiggle/2 + wiggle*2/6
		pwm_5 = S5_init + height/2

		pwm_6 = S6_init - wiggle/2
		pwm_7 = S7_init + height
	elif pos == 4:
		pwm_0 = S0_init - wiggle/2 + wiggle*1/6
		pwm_1 = S1_init - height/2

		pwm_2 = S2_init + wiggle/2 - wiggle*1/6
		pwm_3 = S3_init + height/2

		pwm_4 = S4_init + wiggle/2 + wiggle*3/6
		pwm_5 = S5_init + height/2

		pwm_6 = S6_init - wiggle/2 - wiggle*3/6
		pwm_7 = S7_init - height/2
	elif pos == 5:
		pwm_0 = S0_init - wiggle/2
		pwm_1 = S1_init - height/2

		pwm_2 = S2_init + wiggle/2 - wiggle*2/6
		pwm_3 = S3_init + height/2

		pwm_4 = S4_init + wiggle/2
		pwm_5 = S5_init - height

		pwm_6 = S6_init - wiggle/2 - wiggle*2/6
		pwm_7 = S7_init - height/2
	elif pos == 6:
		pwm_0 = S0_init - wiggle/2 - wiggle*1/6
		pwm_1 = S1_init - height/2

		pwm_2 = S2_init + wiggle/2 - wiggle*3/6
		pwm_3 = S3_init + height/2

		pwm_4 = S4_init + wiggle/2 - wiggle*3/6
		pwm_5 = S5_init + height/2

		pwm_6 = S6_init - wiggle/2 - wiggle*1/6
		pwm_7 = S7_init - height/2
	elif pos == 7:
		pwm_0 = S0_init - wiggle/2 - wiggle*2/6
		pwm_1 = S1_init - height/2

		pwm_2 = S2_init + wiggle/2
		pwm_3 = S3_init - height

		pwm_4 = S4_init + wiggle/2 - wiggle*2/6
		pwm_5 = S5_init + height/2

		pwm_6 = S6_init - wiggle/2
		pwm_7 = S7_init - height/2
	elif pos == 8:
		pwm_0 = S0_init - wiggle/2 - wiggle*3/6
		pwm_1 = S1_init - height/2

		pwm_2 = S2_init + wiggle/2 + wiggle*3/6
		pwm_3 = S3_init + height/2

		pwm_4 = S4_init + wiggle/2 - wiggle*1/6
		pwm_5 = S5_init + height/2

		pwm_6 = S6_init - wiggle/2 + wiggle*1/6
		pwm_7 = S7_init - height/2
		pass
	position_walk.append(int(pwm_0))
	position_walk.append(int(pwm_0))
	position_walk.append(int(pwm_1))
	position_walk.append(int(pwm_2))
	position_walk.append(int(pwm_3))
	position_walk.append(int(pwm_4))
	position_walk.append(int(pwm_5))
	position_walk.append(int(pwm_6))
	position_walk.append(int(pwm_7))
	walk_smooth(position_walk)

def walk_lean(pos, lean):
	wiggle = 100
	height = 100
	position_walk = []
	if pos == 1:
		pwm_0 = S0_init - wiggle/2 
		pwm_1 = S1_init + height - lean

		pwm_2 = S2_init + wiggle/2 + wiggle*2/6
		pwm_3 = S3_init + height/2 - lean

		pwm_4 = S4_init + wiggle/2
		pwm_5 = S5_init + height/2 + lean

		pwm_6 = S6_init - wiggle/2 + wiggle*2/6
		pwm_7 = S7_init - height/2 + lean
	elif pos == 2:
		pwm_0 = S0_init - wiggle/2 + wiggle*3/6
		pwm_1 = S1_init - height/2 - lean

		pwm_2 = S2_init + wiggle/2 + wiggle*1/6
		pwm_3 = S3_init + height/2 - lean

		pwm_4 = S4_init + wiggle/2 + wiggle*1/6
		pwm_5 = S5_init + height/2 + lean

		pwm_6 = S6_init - wiggle/2 + wiggle*3/6
		pwm_7 = S7_init - height/2 + lean
	elif pos == 3:
		pwm_0 = S0_init - wiggle/2 + wiggle*2/6
		pwm_1 = S1_init - height/2 - lean

		pwm_2 = S2_init + wiggle/2
		pwm_3 = S3_init + height/2 - lean

		pwm_4 = S4_init + wiggle/2 + wiggle*2/6
		pwm_5 = S5_init + height/2 + lean

		pwm_6 = S6_init - wiggle/2
		pwm_7 = S7_init + height + lean
	elif pos == 4:
		pwm_0 = S0_init - wiggle/2 + wiggle*1/6
		pwm_1 = S1_init - height/2 - lean

		pwm_2 = S2_init + wiggle/2 - wiggle*1/6
		pwm_3 = S3_init + height/2 - lean

		pwm_4 = S4_init + wiggle/2 + wiggle*3/6
		pwm_5 = S5_init + height/2 + lean

		pwm_6 = S6_init - wiggle/2 - wiggle*3/6
		pwm_7 = S7_init - height/2 + lean
	elif pos == 5:
		pwm_0 = S0_init - wiggle/2
		pwm_1 = S1_init - height/2 - lean

		pwm_2 = S2_init + wiggle/2 - wiggle*2/6
		pwm_3 = S3_init + height/2 - lean

		pwm_4 = S4_init + wiggle/2
		pwm_5 = S5_init - height + lean

		pwm_6 = S6_init - wiggle/2 - wiggle*2/6
		pwm_7 = S7_init - height/2 + lean
	elif pos == 6:
		pwm_0 = S0_init - wiggle/2 - wiggle*1/6
		pwm_1 = S1_init - height/2 - lean

		pwm_2 = S2_init + wiggle/2 - wiggle*3/6
		pwm_3 = S3_init + height/2 - lean

		pwm_4 = S4_init + wiggle/2 - wiggle*3/6
		pwm_5 = S5_init + height/2 + lean

		pwm_6 = S6_init - wiggle/2 - wiggle*1/6
		pwm_7 = S7_init - height/2 + lean
	elif pos == 7:
		pwm_0 = S0_init - wiggle/2 - wiggle*2/6
		pwm_1 = S1_init - height/2 - lean

		pwm_2 = S2_init + wiggle/2
		pwm_3 = S3_init - height - lean

		pwm_4 = S4_init + wiggle/2 - wiggle*2/6
		pwm_5 = S5_init + height/2 + lean

		pwm_6 = S6_init - wiggle/2
		pwm_7 = S7_init - height/2 + lean
	elif pos == 8:
		pwm_0 = S0_init - wiggle/2 - wiggle*3/6
		pwm_1 = S1_init - height/2 - lean

		pwm_2 = S2_init + wiggle/2 + wiggle*3/6
		pwm_3 = S3_init + height/2 - lean

		pwm_4 = S4_init + wiggle/2 - wiggle*1/6
		pwm_5 = S5_init + height/2 + lean

		pwm_6 = S6_init - wiggle/2 + wiggle*1/6
		pwm_7 = S7_init - height/2 + lean
		pass
	position_walk.append(int(pwm_0))
	position_walk.append(int(pwm_0))
	position_walk.append(int(pwm_1))
	position_walk.append(int(pwm_2))
	position_walk.append(int(pwm_3))
	position_walk.append(int(pwm_4))
	position_walk.append(int(pwm_5))
	position_walk.append(int(pwm_6))
	position_walk.append(int(pwm_7))
	walk_smooth(position_walk)

def server_setup():
	global tcpCliSock, pix_input, time_input, speed_input
	HOST = ''
	PORT = 10223							  #Define port serial 
	BUFSIZ = 1024							 #Define buffer size
	ADDR = (HOST, PORT)

	tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcpSerSock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	tcpSerSock.bind(ADDR)
	tcpSerSock.listen(5)					  #Start server,waiting for client
	print('waiting for connection...')
	tcpCliSock, addr = tcpSerSock.accept()
	print('...connected from :', addr)

	def data_servo_ctrl():
		global PWM_0, PWM_1, PWM_2, PWM_3, PWM_4, PWM_5, PWM_6, PWM_7, PWM_8, PWM_9, PWM_10, PWM_11, PWM_12, PWM_13, PWM_14, PWM_15
		if '0+' == data:
			PWM_0 += speed_input
			pwm.set_pwm(0,0,PWM_0)
		elif '0-' ==  data:
			PWM_0 -= speed_input
			pwm.set_pwm(0,0,PWM_0)

		elif '1+' == data:
			PWM_1 += speed_input
			pwm.set_pwm(1,0,PWM_1)
		elif '1-' ==  data:
			PWM_1 -= speed_input
			pwm.set_pwm(1,0,PWM_1)

		elif '2+' == data:
			PWM_2 += speed_input
			pwm.set_pwm(2,0,PWM_2)
		elif '2-' ==  data:
			PWM_2 -= speed_input
			pwm.set_pwm(2,0,PWM_2)

		elif '3+' == data:
			PWM_3 += speed_input
			pwm.set_pwm(3,0,PWM_3)
		elif '3-' ==  data:
			PWM_3 -= speed_input
			pwm.set_pwm(3,0,PWM_3)

		elif '4+' == data:
			PWM_4 += speed_input
			pwm.set_pwm(4,0,PWM_4)
		elif '4-' ==  data:
			PWM_4 -= speed_input
			pwm.set_pwm(4,0,PWM_4)

		elif '5+' == data:
			PWM_5 += speed_input
			pwm.set_pwm(5,0,PWM_5)
		elif '5-' ==  data:
			PWM_5 -= speed_input
			pwm.set_pwm(5,0,PWM_5)

		elif '6+' == data:
			PWM_6 += speed_input
			pwm.set_pwm(6,0,PWM_6)
		elif '6-' ==  data:
			PWM_6 -= speed_input
			pwm.set_pwm(6,0,PWM_6)

		elif '7+' == data:
			PWM_7 += speed_input
			pwm.set_pwm(7,0,PWM_7)
		elif '7-' ==  data:
			PWM_7 -= speed_input
			pwm.set_pwm(7,0,PWM_7)

		elif '8+' == data:
			PWM_8 += speed_input
			pwm.set_pwm(8,0,PWM_8)
		elif '8-' ==  data:
			PWM_8 -= speed_input
			pwm.set_pwm(8,0,PWM_8)

		elif '9+' == data:
			PWM_9 += speed_input
			pwm.set_pwm(9,0,PWM_9)
		elif '9-' ==  data:
			PWM_9 -= speed_input
			pwm.set_pwm(9,0,PWM_9)

		elif '10+' == data:
			PWM_10 += speed_input
			pwm.set_pwm(10,0,PWM_10)
		elif '10-' ==  data:
			PWM_10 -= speed_input
			pwm.set_pwm(10,0,PWM_10)

		elif '11+' == data:
			PWM_11 += speed_input
			pwm.set_pwm(11,0,PWM_11)
		elif '11-' ==  data:
			PWM_11 -= speed_input
			pwm.set_pwm(11,0,PWM_11)

		elif '12+' == data:
			PWM_12 += speed_input
			pwm.set_pwm(12,0,PWM_12)
		elif '12-' ==  data:
			PWM_12 -= speed_input
			pwm.set_pwm(12,0,PWM_12)

		elif '13+' == data:
			PWM_13 += speed_input
			pwm.set_pwm(13,0,PWM_13)
		elif '13-' ==  data:
			PWM_13 -= speed_input
			pwm.set_pwm(13,0,PWM_13)

		elif '14+' == data:
			PWM_14 += speed_input
			pwm.set_pwm(14,0,PWM_14)
		elif '14-' ==  data:
			PWM_14 -= speed_input
			pwm.set_pwm(14,0,PWM_14)

		elif '15+' == data:
			PWM_15 += speed_input
			pwm.set_pwm(15,0,PWM_15)
		elif '15-' ==  data:
			PWM_15 -= speed_input
			pwm.set_pwm(15,0,PWM_15)

		send_all_pwm()
		old_update()

	def data_function_ctrl():
		global function_select
		if 'function_1_on' == data:
			function_select = 'A'
			tcpCliSock.send('function_1_on'.encode())
		elif 'function_2_on' == data:
			function_select = 'B'
			tcpCliSock.send('function_2_on'.encode())
		elif 'function_3_on' == data:
			function_select = 'C'
			tcpCliSock.send('function_3_on'.encode())
		elif 'function_4_on' == data:
			function_select = 'D'
			tcpCliSock.send('function_4_on'.encode())
		elif 'function_5_on' == data:
			function_select = 'E'
			servos.resume()
			tcpCliSock.send('function_5_on'.encode())
		elif 'function_6_on' == data:
			function_select = 'F'
			tcpCliSock.send('function_6_on'.encode())
		elif 'function_7_on' == data:
			function_select = 'G'
			tcpCliSock.send('function_7_on'.encode())

	def data_select_ctrl():
		global position_select
		if 'Select 1' == data:
			position_select = '1:'
			tcpCliSock.send('1 Selected'.encode())

		elif 'Select 2' == data:
			position_select = '2:'
			tcpCliSock.send('2 Selected'.encode())

		elif 'Select 3' == data:
			position_select = '3:'
			tcpCliSock.send('3 Selected'.encode())

		elif 'Select 4' == data:
			position_select = '4:'
			tcpCliSock.send('4 Selected'.encode())

		elif 'Select 5' == data:
			position_select = '5:'
			tcpCliSock.send('5 Selected'.encode())

		elif 'Select 6' == data:
			position_select = '6:'
			tcpCliSock.send('6 Selected'.encode())

		elif 'Select 7' == data:
			position_select = '7:'
			tcpCliSock.send('7 Selected'.encode())

		elif 'Select 8' == data:
			position_select = '8:'
			tcpCliSock.send('8 Selected'.encode())

		elif 'Select 9' == data:
			position_select = '9:'
			tcpCliSock.send('9 Selected'.encode())

		elif 'Select 10' == data:
			position_select = '10:'
			tcpCliSock.send('10 Selected'.encode())

		elif 'Select 11' == data:
			position_select = '11:'
			tcpCliSock.send('11 Selected'.encode())

		elif 'Select 12' == data:
			position_select = '12:'
			tcpCliSock.send('12 Selected'.encode())

		elif 'Select 13' == data:
			position_select = '13:'
			tcpCliSock.send('13 Selected'.encode())

		elif 'Select 14' == data:
			position_select = '14:'
			tcpCliSock.send('14 Selected'.encode())

		elif 'Select 15' == data:
			position_select = '15:'
			tcpCliSock.send('15 Selected'.encode())

		elif 'Select 16' == data:
			position_select = '16:'
			tcpCliSock.send('16 Selected'.encode())

		elif 'Select 17' == data:
			position_select = '17:'
			tcpCliSock.send('17 Selected'.encode())

		elif 'Select 18' == data:
			position_select = '18:'
			tcpCliSock.send('18 Selected'.encode())
		move_input()

	def data_perform_ctrl():

		def perform_1():
			walk(1)
			walk(2)
			walk(3)
			walk(4)
			walk(5)
			walk(6)
			walk(7)
			walk(8)
			walk(7)
			walk(6)
			walk(5)
			walk(4)
			move_config('17:')
			move_config('18:')
			move_config('17:')
			move_config('18:')
			move_config('17:')
			move_config('18:')
			move_config('17:')
			move_config('18:')
			move_config('17:')
			move_config('18:')
			move_config('19:')
			move_config('20:')
			move_config('19:')
			move_config('20:')

		def perform_2():
			for i in range(0,4):
				move_config('21:')
				move_config('22:')
				move_config('21:')
				move_config('22:')
				move_config('23:')
				move_config('24:')
				move_config('23:')
				move_config('24:')

		def perform_3():
			for i in range(0,4):
				move_config('25:')
				move_config('26:')
				move_config('27:')
				move_config('28:')

		def perform_4():
			move_config('29:')
			move_config('30:')
			move_config('31:')
			move_config('32:')
			move_config('31:')
			move_config('30:')
			move_config('29:')

		def perform_5():
			lean_input = -23
			for a in range(0,2):
				for b in range(0,2):
					walk_lean(1,lean_input)
					walk_lean(2,lean_input)
					walk_lean(3,lean_input)
					walk_lean(4,lean_input)
					walk_lean(5,lean_input)
					walk_lean(6,lean_input)
					walk_lean(7,lean_input)
					walk_lean(8,lean_input)
				time.sleep(0.1)
				for c in range(0,2):
					walk_lean(8,-lean_input)
					walk_lean(7,-lean_input)
					walk_lean(6,-lean_input)
					walk_lean(5,-lean_input)
					walk_lean(4,-lean_input)
					walk_lean(3,-lean_input)
					walk_lean(2,-lean_input)
					walk_lean(1,-lean_input)
				time.sleep(0.1)
			init_servos()

		def perform_6():
			for i in range(0,4):
				move_config('33:')
				move_config('34:')
				move_config('33:')
				move_config('35:')
			init_servos()

		def perform_7():
			for i in range(0,3):
				for i in range(0,4):
					move_config('36:')
					move_config('37:')
				for i in range(0,4):
					move_config('38:')
					move_config('39:')
			init_servos()


		def perform_8():
			move_config('2:')

		if 'perform_1' == data:
			tcpCliSock.send('perform_1_on'.encode())
			perform_1()
		elif 'perform_2' == data:
			tcpCliSock.send('perform_2_on'.encode())
			perform_2()
		elif 'perform_3' == data:
			tcpCliSock.send('perform_3_on'.encode())
			perform_3()
		elif 'perform_4' == data:
			tcpCliSock.send('perform_4_on'.encode())
			perform_4()
		elif 'perform_5' == data:
			tcpCliSock.send('perform_5_on'.encode())
			perform_5()
		elif 'perform_6' == data:
			tcpCliSock.send('perform_6_on'.encode())
			perform_6()
		elif 'perform_7' == data:
			tcpCliSock.send('perform_7_on'.encode())
			perform_7()
		elif 'perform_8' == data:
			tcpCliSock.send('perform_8_on'.encode())
			perform_8()
		tcpCliSock.send('perform_end'.encode())

	def set_new_goal():
		goal_to_set = function_select+' '+str(PWM_0)+' '+str(PWM_1)+' '+str(PWM_2)+' '+str(PWM_3)+' '+str(PWM_4)+' '+str(PWM_5)+' '+str(PWM_6)+' '+str(PWM_7)
		goal_to_set = goal_to_set+' '+str(PWM_8)+' '+str(PWM_9)+' '+str(PWM_10)+' '+str(PWM_11)+' '+str(PWM_12)+' '+str(PWM_13)+' '+str(PWM_14)+' '+str(PWM_15)
		replace_num(position_select, goal_to_set)

	while True: 
		data = ''
		data = str(tcpCliSock.recv(BUFSIZ).decode())
		if not data:
			continue

		elif '+' in data or '-' in data:
			data_servo_ctrl()

		elif 'function' in data:
			data_function_ctrl()

		elif 'Select' in data:
			data_select_ctrl()

		elif 'set' == data:
			set_new_goal()

		elif 'perform' in data:
			data_perform_ctrl()

		elif 'pix' in data:
			try:
				set_pix=data.split()
				pix_input = int(set_pix[1])
			except:
				pass
		elif 'time' in data:
			try:
				set_time=data.split()
				time_input = float(set_time[1])
				print(time_input)
			except:
				pass
		elif 'speed' in data:
			try:
				set_speed=data.split()
				speed_to_input = int(set_speed[1])
				if speed_to_input == 0:
					speed_to_input = 1
				speed_input = speed_to_input
			except:
				pass
		print(data)

if __name__ == '__main__':
	pwm = Adafruit_PCA9685.PCA9685()
	pwm.set_pwm_freq(50)

	for i in range(0,16):
		exec('S%d_init=num_import_int("S%d_init:")'%(i,i))
		exec('S%d_min=num_import_int("S%d_min:")'%(i,i))
		exec('S%d_max=num_import_int("S%d_max:")'%(i,i))
		exec('PWM_%d=S%d_init'%(i,i))

	goal_now = []
	old_pwm = []

	pix_input = 10
	time_input = 0
	speed_input = 1

	if_continue = 0

	function_select = 'A'
	position_select = '1:'
	walk_step = 1

	init_servos()

	servos = Servo_ctrl()
	servos.start()
	servos.pause()

	server_setup()

	# try:
	# 	server_setup()
	# except:
	# 	servos.stop()

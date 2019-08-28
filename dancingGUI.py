#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# File name   : client.py
# Description : client
# Author	  : William
# Date		: 2018/08/22

from socket import *
import sys
import time
import threading as thread
import tkinter as tk


ip_stu = 1

def global_init():
	global color_bg, color_text, color_btn, color_line, color_can, color_oval
	color_bg='#000000'		#Set background color
	color_text='#E1F5FE'	  #Set text color
	color_btn='#0277BD'	   #Set button color
	color_line='#01579B'	  #Set line color
	color_can='#212121'	   #Set canvas color
	color_oval='#2196F3'	  #Set oval color

global_init()


def replace_num(initial,new_num):   #Call this function to replace data in '.txt' file
	newline=""
	str_num=str(new_num)
	with open("ip.txt","r") as f:
		for line in f.readlines():
			if(line.find(initial) == 0):
				line = initial+"%s" %(str_num)
			newline += line
	with open("ip.txt","w") as f:
		f.writelines(newline)	#Call this function to replace data in '.txt' file


def num_import(initial):			#Call this function to import data from '.txt' file
	with open("ip.txt") as f:
		for line in f.readlines():
			if(line.find(initial) == 0):
				r=line
	begin=len(list(initial))
	snum=r[begin:]
	n=snum
	return n	


def pwm_show(show_input):
	show_input = show_input.split()
	L0.config(text=show_input[1])
	L1.config(text=show_input[2])
	L2.config(text=show_input[3])
	L3.config(text=show_input[4])
	L4.config(text=show_input[5])
	L5.config(text=show_input[6])
	L6.config(text=show_input[7])
	L7.config(text=show_input[8])
	L8.config(text=show_input[9])
	L9.config(text=show_input[10])
	L10.config(text=show_input[11])
	L11.config(text=show_input[12])
	L12.config(text=show_input[13])
	L13.config(text=show_input[14])
	L14.config(text=show_input[15])
	L15.config(text=show_input[16])


def normal_function_button():
	Btn_function_1.config(bg=color_btn)
	Btn_function_2.config(bg=color_btn)
	Btn_function_3.config(bg=color_btn)
	Btn_function_4.config(bg=color_btn)
	Btn_function_5.config(bg=color_btn)
	Btn_function_6.config(bg=color_btn)
	Btn_function_7.config(bg=color_btn)


def connection_thread():
	while 1:
		car_info = (tcpClicSock.recv(BUFSIZ)).decode()
		if not car_info:
			continue
		elif 'PWM' in car_info:
			pwm_show(car_info)


		elif '1 Selected' == car_info:
			normal_select_button()
			Btn_S1.config(bg='#4CAF50')

		elif '2 Selected' == car_info:
			normal_select_button()
			Btn_S2.config(bg='#4CAF50')

		elif '3 Selected' == car_info:
			normal_select_button()
			Btn_S3.config(bg='#4CAF50')

		elif '4 Selected' == car_info:
			normal_select_button()
			Btn_S4.config(bg='#4CAF50')

		elif '5 Selected' == car_info:
			normal_select_button()
			Btn_S5.config(bg='#4CAF50')

		elif '6 Selected' == car_info:
			normal_select_button()
			Btn_S6.config(bg='#4CAF50')

		elif '7 Selected' == car_info:
			normal_select_button()
			Btn_S7.config(bg='#4CAF50')

		elif '8 Selected' == car_info:
			normal_select_button()
			Btn_S8.config(bg='#4CAF50')

		elif '9 Selected' == car_info:
			normal_select_button()
			Btn_S9.config(bg='#4CAF50')

		elif '10 Selected' == car_info:
			normal_select_button()
			Btn_S10.config(bg='#4CAF50')

		elif '11 Selected' == car_info:
			normal_select_button()
			Btn_S11.config(bg='#4CAF50')

		elif '12 Selected' == car_info:
			normal_select_button()
			Btn_S12.config(bg='#4CAF50')

		elif '13 Selected' == car_info:
			normal_select_button()
			Btn_S13.config(bg='#4CAF50')

		elif '14 Selected' == car_info:
			normal_select_button()
			Btn_S14.config(bg='#4CAF50')

		elif '15 Selected' == car_info:
			normal_select_button()
			Btn_S15.config(bg='#4CAF50')

		elif '16 Selected' == car_info:
			normal_select_button()
			Btn_S16.config(bg='#4CAF50')


		elif 'function_1_on' in car_info:
			normal_function_button()
			Btn_function_1.config(bg='#4CAF50')

		elif 'function_2_on' in car_info:
			normal_function_button()
			Btn_function_2.config(bg='#4CAF50')

		elif 'function_3_on' in car_info:
			normal_function_button()
			Btn_function_3.config(bg='#4CAF50')

		elif 'function_4_on' in car_info:
			normal_function_button()
			Btn_function_4.config(bg='#4CAF50')

		elif 'function_5_on' in car_info:
			normal_function_button()
			Btn_function_5.config(bg='#4CAF50')

		elif 'function_6_on' in car_info:
			normal_function_button()
			Btn_function_6.config(bg='#4CAF50')

		elif 'function_7_on' in car_info:
			normal_function_button()
			Btn_function_7.config(bg='#4CAF50')

		elif 'perform_1_on' in car_info:
			normal_function_button()
			normal_select_button()
			Btn_P1.config(bg='#4CAF50')
		elif 'perform_2_on' in car_info:
			normal_function_button()
			normal_select_button()
			Btn_P2.config(bg='#4CAF50')
		elif 'perform_3_on' in car_info:
			normal_function_button()
			normal_select_button()
			Btn_P3.config(bg='#4CAF50')
		elif 'perform_4_on' in car_info:
			normal_function_button()
			normal_select_button()
			Btn_P4.config(bg='#4CAF50')
		elif 'perform_5_on' in car_info:
			normal_function_button()
			normal_select_button()
			Btn_P5.config(bg='#4CAF50')
		elif 'perform_6_on' in car_info:
			normal_function_button()
			normal_select_button()
			Btn_P6.config(bg='#4CAF50')
		elif 'perform_7_on' in car_info:
			normal_function_button()
			normal_select_button()
			Btn_P7.config(bg='#4CAF50')
		elif 'perform_8_on' in car_info:
			normal_function_button()
			normal_select_button()
			Btn_P8.config(bg='#4CAF50')

		elif 'perform_end' in car_info:
			normal_perform_button()

		print(car_info)


def socket_connect():	 #Call this function to connect with the server
	global ADDR,tcpClicSock,BUFSIZ,ip_stu,ipaddr
	ip_adr=E1.get()	   #Get the IP address from Entry

	if ip_adr == '':	  #If no input IP address in Entry,import a default IP
		ip_adr=num_import('IP:')
		# l_ip_4.config(text='Connecting')
		# l_ip_4.config(bg='#FF8F00')
		# l_ip_5.config(text='Default:%s'%ip_adr)
		pass
	
	SERVER_IP = ip_adr
	SERVER_PORT = 10223   #Define port serial 
	BUFSIZ = 1024		 #Define buffer size
	ADDR = (SERVER_IP, SERVER_PORT)
	tcpClicSock = socket(AF_INET, SOCK_STREAM) #Set connection value for socket

	for i in range (1,6): #Try 5 times if disconnected
		#try:
		if ip_stu == 1:
			print("Connecting to server @ %s:%d..." %(SERVER_IP, SERVER_PORT))
			print("Connecting")
			tcpClicSock.connect(ADDR)		#Connection with the server
		
			print("Connected")
		
			# l_ip_5.config(text='IP:%s'%ip_adr)
			# l_ip_4.config(text='Connected')
			# l_ip_4.config(bg='#558B2F')

			replace_num('IP:',ip_adr)
			E1.config(state='disabled')	  #Disable the Entry
			Btn14.config(state='disabled')   #Disable the Entry
			
			ip_stu=0						 #'0' means connected

			connection_threading=thread.Thread(target=connection_thread)     #Define a thread for connection
			connection_threading.setDaemon(True)							 #'True' means it is a front thread,it would close when the mainloop() closes
			connection_threading.start()									 #Thread starts

			break
		else:
			print("Cannot connecting to server,try it latter!")
			l_ip_4.config(text='Try %d/5 time(s)'%i)
			l_ip_4.config(bg='#EF6C00')
			print('Try %d/5 time(s)'%i)
			ip_stu=1
			time.sleep(1)
			continue

	if ip_stu == 1:
		l_ip_4.config(text='Disconnected')
		l_ip_4.config(bg='#F44336')


def connect(event):	   #Call this function to connect with the server
	if ip_stu == 1:
		sc=thread.Thread(target=socket_connect) #Define a thread for connection
		sc.setDaemon(True)					  #'True' means it is a front thread,it would close when the mainloop() closes
		sc.start()							  #Thread starts


def servo_buttons(x,y):
	global L0, L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15
	def call_pwm0_up(event):
		tcpClicSock.send(('0+').encode())

	def call_pwm0_down(event):
		tcpClicSock.send(('0-').encode())

	def call_pwm1_up(event):
		tcpClicSock.send(('1+').encode())

	def call_pwm1_down(event):
		tcpClicSock.send(('1-').encode())

	def call_pwm2_up(event):
		tcpClicSock.send(('2+').encode())

	def call_pwm2_down(event):
		tcpClicSock.send(('2-').encode())

	def call_pwm3_up(event):
		tcpClicSock.send(('3+').encode())

	def call_pwm3_down(event):
		tcpClicSock.send(('3-').encode())

	def call_pwm4_up(event):
		tcpClicSock.send(('4+').encode())

	def call_pwm4_down(event):
		tcpClicSock.send(('4-').encode())

	def call_pwm5_up(event):
		tcpClicSock.send(('5+').encode())

	def call_pwm5_down(event):
		tcpClicSock.send(('5-').encode())

	def call_pwm6_up(event):
		tcpClicSock.send(('6+').encode())

	def call_pwm6_down(event):
		tcpClicSock.send(('6-').encode())

	def call_pwm7_up(event):
		tcpClicSock.send(('7+').encode())

	def call_pwm7_down(event):
		tcpClicSock.send(('7-').encode())

	def call_pwm8_up(event):
		tcpClicSock.send(('8+').encode())

	def call_pwm8_down(event):
		tcpClicSock.send(('8-').encode())

	def call_pwm9_up(event):
		tcpClicSock.send(('9+').encode())

	def call_pwm9_down(event):
		tcpClicSock.send(('9-').encode())

	def call_pwm10_up(event):
		tcpClicSock.send(('10+').encode())

	def call_pwm10_down(event):
		tcpClicSock.send(('10-').encode())

	def call_pwm11_up(event):
		tcpClicSock.send(('11+').encode())

	def call_pwm11_down(event):
		tcpClicSock.send(('11-').encode())

	def call_pwm12_up(event):
		tcpClicSock.send(('12+').encode())

	def call_pwm12_down(event):
		tcpClicSock.send(('12-').encode())

	def call_pwm13_up(event):
		tcpClicSock.send(('13+').encode())

	def call_pwm13_down(event):
		tcpClicSock.send(('13-').encode())

	def call_pwm14_up(event):
		tcpClicSock.send(('14+').encode())

	def call_pwm14_down(event):
		tcpClicSock.send(('14-').encode())

	def call_pwm15_up(event):
		tcpClicSock.send(('15+').encode())

	def call_pwm15_down(event):
		tcpClicSock.send(('15-').encode())

	L0 = tk.Label(root,width=8,text='PWM0',fg=color_text,bg='#212121')
	L0.place(x=x,y=y-25)
	Btn_0i = tk.Button(root, width=8, text='PWM0+',fg=color_text,bg=color_btn,relief='ridge')
	Btn_0i.place(x=x,y=y)
	Btn_0i.bind('<ButtonPress-1>', call_pwm0_up)

	Btn_0d = tk.Button(root, width=8, text='PWM0-',fg=color_text,bg=color_btn,relief='ridge')
	Btn_0d.place(x=x,y=y+35)
	Btn_0d.bind('<ButtonPress-1>', call_pwm0_down)

	L1 = tk.Label(root,width=8,text='PWM1',fg=color_text,bg='#212121')
	L1.place(x=x+100,y=y-25)
	Btn_1i = tk.Button(root, width=8, text='PWM1+',fg=color_text,bg=color_btn,relief='ridge')
	Btn_1i.place(x=x+100,y=y)
	Btn_1i.bind('<ButtonPress-1>', call_pwm1_up)

	Btn_1d = tk.Button(root, width=8, text='PWM1-',fg=color_text,bg=color_btn,relief='ridge')
	Btn_1d.place(x=x+100,y=y+35)
	Btn_1d.bind('<ButtonPress-1>', call_pwm1_down)

	L2 = tk.Label(root,width=8,text='PWM2',fg=color_text,bg='#212121')
	L2.place(x=x+200,y=y-25)
	Btn_2i = tk.Button(root, width=8, text='PWM2+',fg=color_text,bg=color_btn,relief='ridge')
	Btn_2i.place(x=x+200,y=y)
	Btn_2i.bind('<ButtonPress-1>', call_pwm2_up)

	Btn_2d = tk.Button(root, width=8, text='PWM2-',fg=color_text,bg=color_btn,relief='ridge')
	Btn_2d.place(x=x+200,y=y+35)
	Btn_2d.bind('<ButtonPress-1>', call_pwm2_down)

	L3 = tk.Label(root,width=8,text='PWM3',fg=color_text,bg='#212121')
	L3.place(x=x+300,y=y-25)
	Btn_3i = tk.Button(root, width=8, text='PWM3+',fg=color_text,bg=color_btn,relief='ridge')
	Btn_3i.place(x=x+300,y=y)
	Btn_3i.bind('<ButtonPress-1>', call_pwm3_up)

	Btn_3d = tk.Button(root, width=8, text='PWM3-',fg=color_text,bg=color_btn,relief='ridge')
	Btn_3d.place(x=x+300,y=y+35)
	Btn_3d.bind('<ButtonPress-1>', call_pwm3_down)

	L4 = tk.Label(root,width=8,text='PWM4',fg=color_text,bg='#212121')
	L4.place(x=x+400,y=y-25)
	Btn_4i = tk.Button(root, width=8, text='PWM4+',fg=color_text,bg=color_btn,relief='ridge')
	Btn_4i.place(x=x+400,y=y)
	Btn_4i.bind('<ButtonPress-1>', call_pwm4_up)

	Btn_4d = tk.Button(root, width=8, text='PWM4-',fg=color_text,bg=color_btn,relief='ridge')
	Btn_4d.place(x=x+400,y=y+35)
	Btn_4d.bind('<ButtonPress-1>', call_pwm4_down)

	L5 = tk.Label(root,width=8,text='PWM5',fg=color_text,bg='#212121')
	L5.place(x=x+500,y=y-25)
	Btn_5i = tk.Button(root, width=8, text='PWM5+',fg=color_text,bg=color_btn,relief='ridge')
	Btn_5i.place(x=x+500,y=y)
	Btn_5i.bind('<ButtonPress-1>', call_pwm5_up)

	Btn_5d = tk.Button(root, width=8, text='PWM5-',fg=color_text,bg=color_btn,relief='ridge')
	Btn_5d.place(x=x+500,y=y+35)
	Btn_5d.bind('<ButtonPress-1>', call_pwm5_down)

	L6 = tk.Label(root,width=8,text='PWM6',fg=color_text,bg='#212121')
	L6.place(x=x+600,y=y-25)
	Btn_6i = tk.Button(root, width=8, text='PWM6+',fg=color_text,bg=color_btn,relief='ridge')
	Btn_6i.place(x=x+600,y=y)
	Btn_6i.bind('<ButtonPress-1>', call_pwm6_up)

	Btn_6d = tk.Button(root, width=8, text='PWM6-',fg=color_text,bg=color_btn,relief='ridge')
	Btn_6d.place(x=x+600,y=y+35)
	Btn_6d.bind('<ButtonPress-1>', call_pwm6_down)

	L7 = tk.Label(root,width=8,text='PWM7',fg=color_text,bg='#212121')
	L7.place(x=x+700,y=y-25)
	Btn_7i = tk.Button(root, width=8, text='PWM7+',fg=color_text,bg=color_btn,relief='ridge')
	Btn_7i.place(x=x+700,y=y)
	Btn_7i.bind('<ButtonPress-1>', call_pwm7_up)

	Btn_7d = tk.Button(root, width=8, text='PWM7-',fg=color_text,bg=color_btn,relief='ridge')
	Btn_7d.place(x=x+700,y=y+35)
	Btn_7d.bind('<ButtonPress-1>', call_pwm7_down)


	L8 = tk.Label(root,width=8,text='PWM8',fg=color_text,bg='#212121')
	L8.place(x=x,y=y+75)
	Btn_8i = tk.Button(root, width=8, text='PWM8+',fg=color_text,bg=color_btn,relief='ridge')
	Btn_8i.place(x=x,y=y+100)
	Btn_8i.bind('<ButtonPress-1>', call_pwm8_up)

	Btn_8d = tk.Button(root, width=8, text='PWM8-',fg=color_text,bg=color_btn,relief='ridge')
	Btn_8d.place(x=x,y=y+135)
	Btn_8d.bind('<ButtonPress-1>', call_pwm8_down)

	L9 = tk.Label(root,width=8,text='PWM9',fg=color_text,bg='#212121')
	L9.place(x=x+100,y=y+75)
	Btn_9i = tk.Button(root, width=8, text='PWM9+',fg=color_text,bg=color_btn,relief='ridge')
	Btn_9i.place(x=x+100,y=y+100)
	Btn_9i.bind('<ButtonPress-1>', call_pwm9_up)

	Btn_9d = tk.Button(root, width=8, text='PWM9-',fg=color_text,bg=color_btn,relief='ridge')
	Btn_9d.place(x=x+100,y=y+135)
	Btn_9d.bind('<ButtonPress-1>', call_pwm9_down)

	L10 = tk.Label(root,width=8,text='PWM10',fg=color_text,bg='#212121')
	L10.place(x=x+200,y=y+75)
	Btn_10i = tk.Button(root, width=8, text='PWM10+',fg=color_text,bg=color_btn,relief='ridge')
	Btn_10i.place(x=x+200,y=y+100)
	Btn_10i.bind('<ButtonPress-1>', call_pwm10_up)

	Btn_10d = tk.Button(root, width=8, text='PWM10-',fg=color_text,bg=color_btn,relief='ridge')
	Btn_10d.place(x=x+200,y=y+135)
	Btn_10d.bind('<ButtonPress-1>', call_pwm10_down)

	L11 = tk.Label(root,width=8,text='PWM11',fg=color_text,bg='#212121')
	L11.place(x=x+300,y=y+75)
	Btn_11i = tk.Button(root, width=8, text='PWM11+',fg=color_text,bg=color_btn,relief='ridge')
	Btn_11i.place(x=x+300,y=y+100)
	Btn_11i.bind('<ButtonPress-1>', call_pwm11_up)

	Btn_11d = tk.Button(root, width=8, text='PWM11-',fg=color_text,bg=color_btn,relief='ridge')
	Btn_11d.place(x=x+300,y=y+135)
	Btn_11d.bind('<ButtonPress-1>', call_pwm11_down)

	L12 = tk.Label(root,width=8,text='PWM12',fg=color_text,bg='#212121')
	L12.place(x=x+400,y=y+75)
	Btn_12i = tk.Button(root, width=8, text='PWM12+',fg=color_text,bg=color_btn,relief='ridge')
	Btn_12i.place(x=x+400,y=y+100)
	Btn_12i.bind('<ButtonPress-1>', call_pwm12_up)

	Btn_12d = tk.Button(root, width=8, text='PWM12-',fg=color_text,bg=color_btn,relief='ridge')
	Btn_12d.place(x=x+400,y=y+135)
	Btn_12d.bind('<ButtonPress-1>', call_pwm12_down)

	L13 = tk.Label(root,width=8,text='PWM13',fg=color_text,bg='#212121')
	L13.place(x=x+500,y=y+75)
	Btn_13i = tk.Button(root, width=8, text='PWM13+',fg=color_text,bg=color_btn,relief='ridge')
	Btn_13i.place(x=x+500,y=y+100)
	Btn_13i.bind('<ButtonPress-1>', call_pwm13_up)

	Btn_13d = tk.Button(root, width=8, text='PWM13-',fg=color_text,bg=color_btn,relief='ridge')
	Btn_13d.place(x=x+500,y=y+135)
	Btn_13d.bind('<ButtonPress-1>', call_pwm13_down)

	L14 = tk.Label(root,width=8,text='PWM14',fg=color_text,bg='#212121')
	L14.place(x=x+600,y=y+75)
	Btn_14i = tk.Button(root, width=8, text='PWM14+',fg=color_text,bg=color_btn,relief='ridge')
	Btn_14i.place(x=x+600,y=y+100)
	Btn_14i.bind('<ButtonPress-1>', call_pwm14_up)

	Btn_14d = tk.Button(root, width=8, text='PWM14-',fg=color_text,bg=color_btn,relief='ridge')
	Btn_14d.place(x=x+600,y=y+135)
	Btn_14d.bind('<ButtonPress-1>', call_pwm14_down)


	L15 = tk.Label(root,width=8,text='PWM15',fg=color_text,bg='#212121')
	L15.place(x=x+700,y=y+75)
	Btn_15i = tk.Button(root, width=8, text='PWM15+',fg=color_text,bg=color_btn,relief='ridge')
	Btn_15i.place(x=x+700,y=y+100)
	Btn_15i.bind('<ButtonPress-1>', call_pwm15_up)

	Btn_15d = tk.Button(root, width=8, text='PWM15-',fg=color_text,bg=color_btn,relief='ridge')
	Btn_15d.place(x=x+700,y=y+135)
	Btn_15d.bind('<ButtonPress-1>', call_pwm15_down)


def posSelect_buttons(x,y):
	global Btn_S1, Btn_S2, Btn_S3, Btn_S4, Btn_S5, Btn_S6, Btn_S7, Btn_S8, Btn_S9, Btn_S10, Btn_S11, Btn_S12, Btn_S13, Btn_S14, Btn_S15, Btn_S16
	def select_1(event):
		tcpClicSock.send(('Select 1').encode())

	def select_2(event):
		tcpClicSock.send(('Select 2').encode())

	def select_3(event):
		tcpClicSock.send(('Select 3').encode())

	def select_4(event):
		tcpClicSock.send(('Select 4').encode())

	def select_5(event):
		tcpClicSock.send(('Select 5').encode())

	def select_6(event):
		tcpClicSock.send(('Select 6').encode())

	def select_7(event):
		tcpClicSock.send(('Select 7').encode())

	def select_8(event):
		tcpClicSock.send(('Select 8').encode())


	def select_9(event):
		tcpClicSock.send(('Select 9').encode())

	def select_10(event):
		tcpClicSock.send(('Select 10').encode())

	def select_11(event):
		tcpClicSock.send(('Select 11').encode())

	def select_12(event):
		tcpClicSock.send(('Select 12').encode())

	def select_13(event):
		tcpClicSock.send(('Select 13').encode())

	def select_14(event):
		tcpClicSock.send(('Select 14').encode())

	def select_15(event):
		tcpClicSock.send(('Select 15').encode())

	def select_16(event):
		tcpClicSock.send(('Select 16').encode())


	Btn_S1 = tk.Button(root, width=8, text='Q',fg=color_text,bg=color_btn,relief='ridge')
	Btn_S1.place(x=x,y=y)
	Btn_S1.bind('<ButtonPress-1>', select_1)
	root.bind('<KeyPress-q>', select_1) 

	Btn_S2 = tk.Button(root, width=8, text='W',fg=color_text,bg=color_btn,relief='ridge')
	Btn_S2.place(x=x+100,y=y)
	Btn_S2.bind('<ButtonPress-1>', select_2)
	root.bind('<KeyPress-w>', select_2)

	Btn_S3 = tk.Button(root, width=8, text='E',fg=color_text,bg=color_btn,relief='ridge')
	Btn_S3.place(x=x+200,y=y)
	Btn_S3.bind('<ButtonPress-1>', select_3)
	root.bind('<KeyPress-e>', select_3) 

	Btn_S4 = tk.Button(root, width=8, text='R',fg=color_text,bg=color_btn,relief='ridge')
	Btn_S4.place(x=x+300,y=y)
	Btn_S4.bind('<ButtonPress-1>', select_4)
	root.bind('<KeyPress-r>', select_4) 

	Btn_S5 = tk.Button(root, width=8, text='T',fg=color_text,bg=color_btn,relief='ridge')
	Btn_S5.place(x=x+400,y=y)
	Btn_S5.bind('<ButtonPress-1>', select_5)
	root.bind('<KeyPress-t>', select_5) 

	Btn_S6 = tk.Button(root, width=8, text='Y',fg=color_text,bg=color_btn,relief='ridge')
	Btn_S6.place(x=x+500,y=y)
	Btn_S6.bind('<ButtonPress-1>', select_6)
	root.bind('<KeyPress-y>', select_6) 

	Btn_S7 = tk.Button(root, width=8, text='U',fg=color_text,bg=color_btn,relief='ridge')
	Btn_S7.place(x=x+600,y=y)
	Btn_S7.bind('<ButtonPress-1>', select_7)
	root.bind('<KeyPress-u>', select_7) 

	Btn_S8 = tk.Button(root, width=8, text='I',fg=color_text,bg=color_btn,relief='ridge')
	Btn_S8.place(x=x+700,y=y)
	Btn_S8.bind('<ButtonPress-1>', select_8)
	root.bind('<KeyPress-i>', select_8) 


	Btn_S9 = tk.Button(root, width=8, text='A',fg=color_text,bg=color_btn,relief='ridge')
	Btn_S9.place(x=x,y=y+35)
	Btn_S9.bind('<ButtonPress-1>', select_9)
	root.bind('<KeyPress-a>', select_9)

	Btn_S10 = tk.Button(root, width=8, text='S',fg=color_text,bg=color_btn,relief='ridge')
	Btn_S10.place(x=x+100,y=y+35)
	Btn_S10.bind('<ButtonPress-1>', select_10)
	root.bind('<KeyPress-s>', select_10) 

	Btn_S11 = tk.Button(root, width=8, text='D',fg=color_text,bg=color_btn,relief='ridge')
	Btn_S11.place(x=x+200,y=y+35)
	Btn_S11.bind('<ButtonPress-1>', select_11)
	root.bind('<KeyPress-d>', select_11) 

	Btn_S12 = tk.Button(root, width=8, text='F',fg=color_text,bg=color_btn,relief='ridge')
	Btn_S12.place(x=x+300,y=y+35)
	Btn_S12.bind('<ButtonPress-1>', select_12)
	root.bind('<KeyPress-f>', select_12) 

	Btn_S13 = tk.Button(root, width=8, text='G',fg=color_text,bg=color_btn,relief='ridge')
	Btn_S13.place(x=x+400,y=y+35)
	Btn_S13.bind('<ButtonPress-1>', select_13)
	root.bind('<KeyPress-g>', select_13) 

	Btn_S14 = tk.Button(root, width=8, text='H',fg=color_text,bg=color_btn,relief='ridge')
	Btn_S14.place(x=x+500,y=y+35)
	Btn_S14.bind('<ButtonPress-1>', select_14)
	root.bind('<KeyPress-h>', select_14) 

	Btn_S15 = tk.Button(root, width=8, text='J',fg=color_text,bg=color_btn,relief='ridge')
	Btn_S15.place(x=x+600,y=y+35)
	Btn_S15.bind('<ButtonPress-1>', select_15)
	root.bind('<KeyPress-j>', select_15) 

	Btn_S16 = tk.Button(root, width=8, text='K',fg=color_text,bg=color_btn,relief='ridge')
	Btn_S16.place(x=x+700,y=y+35)
	Btn_S16.bind('<ButtonPress-1>', select_16)
	root.bind('<KeyPress-k>', select_16) 


def perform_buttons(x,y):
	global Btn_P1, Btn_P2, Btn_P3, Btn_P4, Btn_P5, Btn_P6, Btn_P7, Btn_P8
	def perform_1(event):
		tcpClicSock.send(('perform_1').encode())
	def perform_2(event):
		tcpClicSock.send(('perform_2').encode())
	def perform_3(event):
		tcpClicSock.send(('perform_3').encode())
	def perform_4(event):
		tcpClicSock.send(('perform_4').encode())
	def perform_5(event):
		tcpClicSock.send(('perform_5').encode())
	def perform_6(event):
		tcpClicSock.send(('perform_6').encode())
	def perform_7(event):
		tcpClicSock.send(('perform_7').encode())
	def perform_8(event):
		tcpClicSock.send(('perform_8').encode())

	Btn_P1 = tk.Button(root, width=8, text='Perform_1',fg=color_text,bg=color_btn,relief='ridge')
	Btn_P1.place(x=x,y=y)
	Btn_P1.bind('<ButtonPress-1>', perform_1)
	root.bind('<KeyPress-z>', perform_1)

	Btn_P2 = tk.Button(root, width=8, text='Perform_2',fg=color_text,bg=color_btn,relief='ridge')
	Btn_P2.place(x=x+100,y=y)
	Btn_P2.bind('<ButtonPress-1>', perform_2)
	root.bind('<KeyPress-x>', perform_2)

	Btn_P3 = tk.Button(root, width=8, text='Perform_3',fg=color_text,bg=color_btn,relief='ridge')
	Btn_P3.place(x=x+200,y=y)
	Btn_P3.bind('<ButtonPress-1>', perform_3)
	root.bind('<KeyPress-c>', perform_3)

	Btn_P4 = tk.Button(root, width=8, text='Perform_4',fg=color_text,bg=color_btn,relief='ridge')
	Btn_P4.place(x=x+300,y=y)
	Btn_P4.bind('<ButtonPress-1>', perform_4)
	root.bind('<KeyPress-v>', perform_4)

	Btn_P5 = tk.Button(root, width=8, text='Perform_5',fg=color_text,bg=color_btn,relief='ridge')
	Btn_P5.place(x=x+400,y=y)
	Btn_P5.bind('<ButtonPress-1>', perform_5)
	root.bind('<KeyPress-b>', perform_5)

	Btn_P6 = tk.Button(root, width=8, text='Perform_6',fg=color_text,bg=color_btn,relief='ridge')
	Btn_P6.place(x=x+500,y=y)
	Btn_P6.bind('<ButtonPress-1>', perform_6)
	root.bind('<KeyPress-n>', perform_6)

	Btn_P7 = tk.Button(root, width=8, text='Perform_7',fg=color_text,bg=color_btn,relief='ridge')
	Btn_P7.place(x=x+600,y=y)
	Btn_P7.bind('<ButtonPress-1>', perform_7)
	root.bind('<KeyPress-m>', perform_7)

	Btn_P8 = tk.Button(root, width=8, text='Perform_8',fg=color_text,bg=color_btn,relief='ridge')
	Btn_P8.place(x=x+700,y=y)
	Btn_P8.bind('<ButtonPress-1>', perform_8)
	root.bind('<KeyPress-,>', perform_8)


def normal_perform_button():
	Btn_P1.config(bg=color_btn)
	Btn_P2.config(bg=color_btn)
	Btn_P3.config(bg=color_btn)
	Btn_P4.config(bg=color_btn)
	Btn_P5.config(bg=color_btn)
	Btn_P6.config(bg=color_btn)
	Btn_P7.config(bg=color_btn)
	Btn_P8.config(bg=color_btn)


def normal_select_button():
	Btn_S1.config(bg=color_btn)
	Btn_S2.config(bg=color_btn)
	Btn_S3.config(bg=color_btn)
	Btn_S4.config(bg=color_btn)
	Btn_S5.config(bg=color_btn)
	Btn_S6.config(bg=color_btn)
	Btn_S7.config(bg=color_btn)
	Btn_S8.config(bg=color_btn)
	Btn_S9.config(bg=color_btn)
	Btn_S10.config(bg=color_btn)
	Btn_S11.config(bg=color_btn)
	Btn_S12.config(bg=color_btn)
	Btn_S13.config(bg=color_btn)
	Btn_S14.config(bg=color_btn)
	Btn_S15.config(bg=color_btn)
	Btn_S16.config(bg=color_btn)


def connent_input(x,y):
	global E1, Btn14
	E1 = tk.Entry(root,show=None,width=16,bg="#37474F",fg='#eceff1')
	E1.place(x=x+5,y=y+25)							 #Define a Entry and put it in position

	l_ip_3=tk.Label(root,width=10,text='IP Address:',fg=color_text,bg='#000000')
	l_ip_3.place(x=x,y=y)						 #Define a Label and put it in position

	Btn14= tk.Button(root, width=8,height=2, text='Connect',fg=color_text,bg=color_btn,relief='ridge')
	Btn14.place(x=x+130,y=y)						  #Define a Button and put it in position

	root.bind('<Return>', connect)
	Btn14.bind('<ButtonPress-1>', connect)


def set_button(x,y):
	def call_Switch_1(event):
		tcpClicSock.send(('set').encode())

	global L_select_feedback
	L_select_feedback = tk.Label(root,width=10,text='Selected',fg=color_text,bg='#000000')
	L_select_feedback.place(x=x-80,y=y)

	Btn_Switch_1 = tk.Button(root, width=8, text='SET',fg=color_text,bg=color_btn,relief='ridge')
	Btn_Switch_1.place(x=x,y=y)
	Btn_Switch_1.bind('<ButtonPress-1>', call_Switch_1)


def scale(x,y,w):
	def pix_send(event):
		time.sleep(0.03)
		tcpClicSock.send(('pix %s'%var_B.get()).encode())


	def time_send(event):
		time.sleep(0.03)
		tcpClicSock.send(('time %s'%var_C.get()).encode())

	global var_B, var_C
	var_B = tk.StringVar()
	var_B.set(10)

	var_C = tk.StringVar()
	var_C.set(0.03)

	Scale_B = tk.Scale(root,label=None,
	from_=0,to=50,orient=tk.HORIZONTAL,length=w,
	showvalue=1,tickinterval=None,resolution=5,variable=var_B,troughcolor='#448AFF',command=pix_send,fg=color_text,bg=color_bg,highlightthickness=0)
	Scale_B.place(x=x,y=y)							#Define a Scale and put it in position

	Scale_B = tk.Scale(root,label=None,
	from_=0.00,to=0.15,orient=tk.HORIZONTAL,length=w,
	showvalue=1,tickinterval=None,resolution=0.01,variable=var_C,troughcolor='#448AFF',command=time_send,fg=color_text,bg=color_bg,highlightthickness=0)
	Scale_B.place(x=x,y=y+30)							#Define a Scale and put it in position

	canvas_cover=tk.Canvas(root,bg=color_bg,height=30,width=510,highlightthickness=0)
	canvas_cover.place(x=x,y=y+60)


def speed_set(x,y,w):
	def speed_send(event):
		time.sleep(0.03)
		tcpClicSock.send(('speed %s'%var_speed.get()).encode())
	global var_speed
	var_speed = tk.StringVar()
	var_speed.set(1)

	Scale_speed = tk.Scale(root,label=None,
	from_=1,to=50,orient=tk.HORIZONTAL,length=w,
	showvalue=1,tickinterval=None,resolution=1,variable=var_speed,troughcolor='#448AFF',command=speed_send,fg=color_text,bg=color_bg,highlightthickness=0)
	Scale_speed.place(x=x,y=y)							#Define a Scale and put it in position


def function_buttons(x,y):
	global function_stu, Btn_function_1, Btn_function_2, Btn_function_3, Btn_function_4, Btn_function_5, Btn_function_6, Btn_function_7
	def call_function_1(event):
		tcpClicSock.send(('function_1_on').encode())

	def call_function_2(event):
		tcpClicSock.send(('function_2_on').encode())

	def call_function_3(event):
		tcpClicSock.send(('function_3_on').encode())

	def call_function_4(event):
		tcpClicSock.send(('function_4_on').encode())

	def call_function_5(event):
		tcpClicSock.send(('function_5_on').encode())

	def call_function_6(event):
		tcpClicSock.send(('function_6_on').encode())

	def call_function_7(event):
		tcpClicSock.send(('function_7_on').encode())

	Btn_function_1 = tk.Button(root, width=8, text='FastMove',fg=color_text,bg=color_btn,relief='ridge')
	Btn_function_2 = tk.Button(root, width=8, text='Smooth',fg=color_text,bg=color_btn,relief='ridge')
	Btn_function_3 = tk.Button(root, width=8, text='Bézier',fg=color_text,bg=color_btn,relief='ridge')
	Btn_function_4 = tk.Button(root, width=8, text='Config',fg=color_text,bg=color_btn,relief='ridge')
	Btn_function_5 = tk.Button(root, width=8, text='-',fg=color_text,bg=color_btn,relief='ridge')
	Btn_function_6 = tk.Button(root, width=8, text='-',fg=color_text,bg=color_btn,relief='ridge')
	Btn_function_7 = tk.Button(root, width=8, text='-',fg=color_text,bg=color_btn,relief='ridge')

	Btn_function_1.place(x=x,y=y)
	Btn_function_2.place(x=x+70,y=y)
	Btn_function_3.place(x=x+140,y=y)
	Btn_function_4.place(x=x+210,y=y)
	Btn_function_5.place(x=x+280,y=y)
	Btn_function_6.place(x=x+350,y=y)
	Btn_function_7.place(x=x+420,y=y)

	Btn_function_1.bind('<ButtonPress-1>', call_function_1)
	Btn_function_2.bind('<ButtonPress-1>', call_function_2)
	Btn_function_3.bind('<ButtonPress-1>', call_function_3)
	Btn_function_4.bind('<ButtonPress-1>', call_function_4)
	Btn_function_5.bind('<ButtonPress-1>', call_function_5)
	Btn_function_6.bind('<ButtonPress-1>', call_function_6)
	Btn_function_7.bind('<ButtonPress-1>', call_function_7)


def loop():
	global root
	root = tk.Tk()			
	root.title('GWR-R GUI')
	root.geometry('825x520')
	root.config(bg=color_bg)

	try:
		logo =tk.PhotoImage(file = 'logo.png')
		l_logo=tk.Label(root,image = logo,bg=color_bg)
		l_logo.place(x=30,y=13)
	except:
		pass

	connent_input(125,15)

	set_button(730,35)

	speed_set(350,25,280)

	servo_buttons(30,120)

	posSelect_buttons(30,385)

	perform_buttons(30,465)

	scale(530,290,260)

	function_buttons(30,320)

	root.mainloop()


if __name__ == '__main__':
	loop()
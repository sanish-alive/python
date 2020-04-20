import time
import os

os.system('cls')
os.system('color a')
os.system('title Time')

def timing():
	s=0
	m=0
	h=0
	while True:
		time.sleep(1)
		s+=1
		if s==60:
			m+=1
			s=0
			if m==60:
				h+=1
				m=0
		os.system('cls')
		print(h," hour: ",m," minute: ",s," second")

timing()
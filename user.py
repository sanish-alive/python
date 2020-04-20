import requests
import random
import os
l=0
while True:
	l+=1
	print(l)
	ran_num1 =str(random.randrange(10,255))
	ran_num2 =str(random.randrange(10,255))
	ran_num3 =str(random.randrange(10,255))
	ran_num4 =str(random.randrange(10,255))
	ran_num = ran_num1+'.'+ran_num2+'.'+ran_num3+'.'+ran_num4
	ip=str(ran_num)
	try:
		req = requests.get('http://'+ip)
		if req.status_code == 200:
			print(ip+ ' is online')
			os.system("start Kalimba.mp3")

		else:
			print(ip+' id offline')
	except:
		print(ip+' unable to connect')
	if l==1000:
		break
os.system("start Kalimba.mp3")	
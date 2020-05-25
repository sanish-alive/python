import requests, os

sec_ip='200'
ip=10

while True:
        r = os.system(f'ping -n 1 10.129.{sec_ip}.{ip}')
        if r==0:
                print(ip,' found')
                os.system("start Kalimba.mp3")
                input()
                 
        elif r==1:
                print(ip,' not found')
        else:
                print('something went wrong')
        ip+=1


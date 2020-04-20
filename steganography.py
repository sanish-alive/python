from PIL import Image
import stepic
'''image extention should be in jpg to encode 
and png to decode'''

def encode():
	try:
		im_name=str(input('Enter your image name with extension: '))
		im=Image.open(im_name)
		msg=str(input("Enter your msg: "))
		im1=stepic.encode(im, msg.encode())
		ex_split = im_name.split('.')
		modify_img_name=ex_split[0]+'_encode'+'.png'
		im1.save(modify_img_name)

		im1=Image.open(modify_img_name)
		im1.show()
	except:
		print('something went wrong')


def decode():
	try:
		im2=Image.open(str(input('Enter your image name with extension: ')))
		stegoImage=stepic.decode(im2)
		print(stegoImage)
	except:
		print('something went wrong')

def main():
	print('1. encode\n2. Decode')
	user = str(input('Enter num: '))
	if user=='1':
		encode()
	elif user=='2':
		decode()
	elif len(user)==0:
		print('you did enter any value')
		input('Press Enter')
		main()
	else:
		print('You enter wrong value')
		input('Press Enter')
		main()

main()
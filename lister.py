from os import walk
lol=str('D:\\python project\\flaskr')
for filename in walk(lol):
	print(filename)

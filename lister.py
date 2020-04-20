from os import walk
lol=str('C:\\Users\\kotako\\Desktop\\flaskr')
for filename in walk(lol):
	print(filename)
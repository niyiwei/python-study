filename = 'alice.txt'

#处理FileNotFoundError异常
try:
	with open(filename) as fObj:
		contents = fObj.read();
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)
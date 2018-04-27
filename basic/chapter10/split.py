#split()以空格为分隔符将字符串拆成多个部分
# title = "Alice in Wonderland"
# arr = title.split()
# print(arr)

fileName = 'alice.txt'
try:
	with open(fileName,"r") as fObj:
		contents = fObj.read()
except FileNotFoundError:
	msg = "Sorry, the file "+ fileName + " does not exist.";
	print(msg);
else:
	# 计算文件大致包含多少个单词
	words = contents.split()
	numWords = len(words)
	print("The file "+ fileName + " has about "+ str(numWords)+" words.")

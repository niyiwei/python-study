def countWords(fileName):
	try:
		with open(fileName,"r") as fObj:
			contents = fObj.read()
	except FileNotFoundError:
		#pass语句，可以在代码快中使用它来让Python什么都不做
		pass
		# msg = "Sorry, the file "+ fileName + " does not exist.";
		# print(msg);
	else:
		# 计算文件大致包含多少个单词
		words = contents.split()
		numWords = len(words)
		print("The file "+ fileName + " has about "+ str(numWords)+" words.")

# fileName = "alice.txt"
# countWords(fileName)
fileNames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_woman.txt']
for file in fileNames:
	countWords(file)
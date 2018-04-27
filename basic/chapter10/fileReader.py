#从文件中读取数据
# with open('piDigits.txt') as fileObject:
# 	contents = fileObject.read()
# 	print("--"+contents+"--")

fileName = "piDigits.txt"
#逐行读取
# with open(fileName) as fileObject:
# 	for line in fileObject:
# 		print(line.rstrip());

# 创建一个包含文件合行内容的列表
with open(fileName) as fileObject:
	lines = fileObject.readlines();

for line in lines:
	print(line.rstrip())
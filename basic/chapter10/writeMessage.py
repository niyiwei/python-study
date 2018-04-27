filename = 'programming.txt'

#open 提供了实参，第一个是文件名称，第二个是执行的模式(r:读取模式),(w:写入模式),(a:追加模式)
#默认时读取模式
with open(filename, 'a') as fileObject:
	#\n是换行符
	fileObject.write("I also love finding meaning in large datasets.\n")
	fileObject.write("I love creating apps that can run in a browser.\n")
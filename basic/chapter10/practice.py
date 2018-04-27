#决定报告哪些错误 练习

#10-6 10-6 加法运算 ：提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数字。在这种情况下，当你尝试将输入转换为整数时，将引
#发TypeError 异常。编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。在用户输入的任何一个值不是数字时都捕获TypeError 异常，并打印一
#条友好的错误消息。对你编写的程序进行测试：先输入两个数字，再输入一些文本而不是数字。

# countA = input("请输入第一个数：")
# countB = input("请输入第二个数：")
# try:
# 	result = int(countA) + int(countB)
# except ValueError:
# 	print("\n错误提示：请输入数字哟")
# else:
# 	print("结果为: "+str(result))

#10-7将你为完成练习10-6而编写的代码放在一个while 循环中，让用户犯错（输入的是文本而不是数字）后能够继续输入数字
# def inputDigit():
# 	while True:
# 		try:
# 			result = int(input("请输入要进行相加的数字: "));
# 		except ValueError:
# 			print("输入错误！")
# 		else:
# 			return result;
# countA = inputDigit();
# countB = inputDigit();
# print(str(countA) + " + " + str(countB) + " = " + str(countA+countB))

#10-8 猫和狗 ：创建两个文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。编写一个程序，尝试读取这些文件，
#并将其内容打印到屏幕上。将这些代码放在一个try-except 代码块中，以便在文件不存在时捕获FileNotFound 错误，并打印一条友好的消息。将其中一个文件
#移到另一个地方，并确认except 代码块中的代码将正确地执行。

fileNames = ['cat.txt', 'dog.txt']
for fileName in fileNames:
	try:
		with open(fileName) as fObj:
			print(fObj.read());
	except FileNotFoundError:
		#使用pass则可以不执行任何操作
		pass
		# msg = "Sorry, the file " + fileName + " does not exist."
		# print(msg)
#7.3 使用标记


#7.2.4 使用break退出循环

#函数input()的工作原理
#input()函数接受一个参数：即要向用户显示的提示或说明，让用户明白该如何做
# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# while Ture:
# 	message = input(prompt)
# 	if(message != 'quit'):
# 		print(message)
# 	else:
# 		break


#7.2.5 在循环中使用continue
currentNumber = 0
while currentNumber < 10:
	currentNumber += 1
	if currentNumber % 2 == 0:
		continue
	print(currentNumber)
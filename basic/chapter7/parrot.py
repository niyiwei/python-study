#函数input()的工作原理
#input()函数接受一个参数：即要向用户显示的提示或说明，让用户明白该如何做
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
	message = input(prompt)
	if(message != 'quit'):
		print(message)
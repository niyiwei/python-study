#异常

#使用try-except代码快
# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print("You can't divide by zero!")

#使用异常避免崩溃
print("Give me two numbers. and I'll divide them.")
print("Enter 'q' to quit.")
while True:
	firstNumber = input("\nFirst number: ")
	if firstNumber == 'q':
		break
	secondNumber = input("Second number: ")
	if secondNumber == 'q':
		break
	try:
		answer = int(firstNumber) / int(secondNumber)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	#依赖于try 代码快成功的代码都应放到else代码块中
	else:
		print(answer)
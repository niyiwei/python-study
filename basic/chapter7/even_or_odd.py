# 求模运算符 % 将两个数相除并返回余数：
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
	print("\nThe number "+ str(number) + " is even.")
else:
	print("\nThe number "+ str(number) + " is odd.")
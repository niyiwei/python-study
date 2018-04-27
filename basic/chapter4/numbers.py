#Python函数range() 让你能够轻松的生成一系列的数字。
#range()函数从指定的第一个值开始数，并在到达你指定的第二个值后停止
#range(1,5) 打印 1,2,3,4
for value in range(1,5):
	print(value)

#使用range()创建数字列表
#list()方法可以转为列表
numbers = list(range(1,5))
print(numbers)
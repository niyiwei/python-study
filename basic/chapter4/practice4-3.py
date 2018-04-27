#动手试一试
#4-3 数到20 ：使用一个for 循环打印数字1~20（含）。
for value in range(1,21):
	print(value)
#4-4 一百万 ：创建一个列表，其中包含数字1~1 000 000，再使用一个for 循环将这些数字打印出来（如果输出的时间太长，按Ctrl + C停止输出，或关闭输出窗口）。
digits = range(1,1000001)
# for value in digits:
# 	print(value)
#4-5 计算1~1 000 000的总和 ：创建一个列表，其中包含数字1~1 000 000，再使用min() 和max() 核实该列表确实是从1开始，到1 000 000结束的。另外，对这个列表调用函数sum() ，看看Python将一百万个数字相加需要多长时间。
digits = list(range(1,1000001))
print("最小值:"+ str(min(digits)))
print("最大值:"+ str(max(digits)))
print("总和值:"+ str(sum(digits)))
#4-6 奇数 ：通过给函数range() 指定第三个参数来创建一个列表，其中包含1~20的奇数；再使用一个for 循环将这些数字都打印出来。
numberList = list(range(1,21,2))
for value in numberList :
	print(value)
#4-7 3的倍数 ：创建一个列表，其中包含3~30内能被3整除的数字；再使用一个for 循环将这个列表中的数字都打印出来。
numberList = range(3,30,3)
for value in numberList :
	print(value)
#4-8 立方 ：将同一个数字乘三次称为立方。例如，在Python中，2的立方用2**3 表示。请创建一个列表，其中包含前10个整数（即1~10）的立方，再使用一个for 循环将这些立方数都打印出来。
numberList = []
for value in range(1,11):
	numberList.append(value**3)
for value in numberList :
	print(value)
#4-9 立方解析 ：使用列表解析生成一个列表，其中包含前10个整数的立方。
numberList = [value ** 3 for value in range(1,11)]
for value in numberList :
	print(value)
#在Python中不可修改的列表称之为元组
#定义元组列表使用园括号定义,不是方括号哟
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#尝试改一下值
# print("Try change list first value...")
# dimensions[1] = 222
# print(dimensions)


#修改元组变量
#虽然不能修改元组的元素,但可以给存储元组的变量赋值。因此，如果要修改前述矩阵的尺寸，可重新定义整个元组
dimensions = (5,6)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)


dimensions = (100,600)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
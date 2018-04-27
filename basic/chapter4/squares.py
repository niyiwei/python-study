#Python中，两个星号(**)表示乘方运算
#演示如何将10个整数的平方加入到一个列表中
squares = []
for value in range(1,11):
	#星号后面的数值代表乘方的数 如: 2 ** 2 = 2的2次方
	squares.append(value **2)

print(squares)


#对数字列表执行简单的统计计算
#求数字列表最大值:max(digitsList),最小值:min(digitsList),求和:sum(digitsList)
digits = [1,2,3,4,5,6,7,8,9,0]
print(max(digits))
print(min(digits))
print(sum(digits))


#列表解析
#上面所生成列表需要三四行代码，而列表解析让你只需要写一行代码就能生成这样的列表
#解析
#列表名 - [] 表示列表 - 里面定义为表达式:value ** 2计算平方值. 接下来 编写for循环，用于给表达式提供值 ：注意！for后面没有冒号(:)
squares = [ value ** 2 for value in range(1,11)]
print(squares)



#4.4 使用列表的一部分
#4.4.1 切片
#跟range函数一样，Python在到达你指定的第二个索引前面的元素后停止
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
#如果前面的下标不输入则默认从头开始
print(players[:3])
#如果后面的下标不输入则默认到尾部
print(players[2:])
#如果只想输出后面的几位则开头可以为负数
print(players[-2:])

#4.4.2 遍历切片
print("Here are the first three players on my team:")
for player in players[0:3]:
	print(player)


#4.4.3 复制列表
foods = ['baozi','mantou','yumi','jitui']
#想要复制列表跟以前的列表没有关联使用 foods[:]
likeFoods = foods[:]
foods.append("ganliang")
print(foods)
print(likeFoods)

#使用 likeFoods = foods 行不通会有关联
eatFoods = foods;
foods.append("yu")
print(foods)
print(eatFoods)
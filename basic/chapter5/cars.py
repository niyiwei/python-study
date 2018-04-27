cars = ['audi', 'bmw', 'subaru', 'toyoto']

#使用if判断
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car)

#多个判断条件  if xx ==xx and xx == xx

#只有要一个满足使用 if xx ==xx or xx == xx

#检查特定值是否包含在列表中  in   'xx' in xxList

#检查特定值是否不包含在列表中 not in |   if user not in bannedUsers


car = 'subaru'

print("Is car == 'subaru'? I predict Ture.")
print(car == 'audi')


#if的写法
if 1 == 1 :
	print("1=1")
else:
	print("budengyu")

#还可以写成 if-elif-else结构
if 1 == 1:
	print("1=1")
elif 2 ==2:
	print("2 = 2")
else:
	print("都不等于")

#多个elif  if-elif-elif-elif-else
if 1 == 1:
	print("1=1")
elif 2 ==2:
	print("2 = 2")
elif 3 ==3:
	print("3 = 3")
elif 4 ==4:
	print("4 = 4")
else:
	print("都不等于")

#省略else
if 1 == 1:
	print("1=1")
elif 2 ==2:
	print("2 = 2")
#3.3 组织列表
#3.3.1 使用方法sort()对列表进行永久性排序

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)

#反向排序 向sort()方法传递参数 reverse=True


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#使用函数sorted() 对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted　list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)


#倒叙列表
#使用reverse()方法，永久性的
cars = ['a', 'b', 'c', 'd']
cars.reverse()
print(cars)

#获取列表的长度
#使用len()方法获取列表长度
cars = ['a', 'b', 'c', 'd']
print(len(cars))
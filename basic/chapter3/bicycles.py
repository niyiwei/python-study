#列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized'];
print(bicycles);

#访问列表的元素
print(bicycles[0])

#可以使用字符串的方法
print(bicycles[0].title())

#列表的索引是从0开始的

#修改，添加，删除元素
print("修改前")
print(bicycles)
print("修改后")
bicycles[0] = 'moto'
print(bicycles)

#在列表末尾添加元素
print("添加前")
print(bicycles)
print("添加后")
bicycles.append('Air')
print(bicycles)

#列表中插入元素
bicycles.insert(0,'tank')
print(bicycles)

#删除元素
#1、知道元素位置删除
del bicycles[1]
print(bicycles)

#2、从列表末尾删除
lastObject = bicycles.pop()
print(bicycles)
print(lastObject)

#3、弹出列表任何位置的元素
removeObject = bicycles.pop(3)
print(bicycles)
print(removeObject)


#4、根据值删除元素
print("\n根据值删除元素")
nameList = ['A', 'B', 'C', 'D', 'E']
removeName = nameList.remove('B')
print(removeName)
print(nameList)
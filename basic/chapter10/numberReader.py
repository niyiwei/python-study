import json

fileName = 'numbers.json'

with open(fileName, "r") as fObj:
	#使用json.load()函数加载json文件中的数据
	numbers = json.load(fObj)
print(numbers)
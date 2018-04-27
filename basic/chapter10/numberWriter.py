import json

numbers = [2,3,5,7,11,13]

fileName = 'numbers.json'
with open(fileName, 'w') as fObj:
	#使用函数json.dump将数字列表存储在json文件中
	json.dump(numbers, fObj);
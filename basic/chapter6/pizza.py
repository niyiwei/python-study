#在字典中存储列表

#存储所点披萨的信息
pizza = {
	'crust': 'thick'
	,'toppings' : ['mushrooms', 'extra cheese']
}

#概述所点的披萨
print("You ordered a "+ pizza['crust'] + "-crust pizza "+ "with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)


#字典里面存储字典
userInfo = {
	'username': 'xiaoming'
	,'address': {
		'zip':'6000'
		,'str' : '哈哈哈'
	}
}
print(str(userInfo))
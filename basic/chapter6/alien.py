#一个简单的字典
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#字典的结构跟JavaScript的对象结构操作类似


#遍历字典
user_0 = {
	'username' : 'efermi'
	,'first': 'enrico'
	,'last': 'fermi'
}
for key, value in user_0.items():
	print("\nKey:"+key)
	print("Value:"+value)
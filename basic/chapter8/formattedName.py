#8.3 返回值
def getFormattedName(firstName, lastName):
	#返回整洁的姓名
	fullNmae = firstName + ' ' + lastName
	return fullNmae.title()

musician = getFormattedName("jimi", 'hendrix')
print(musician)
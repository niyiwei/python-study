def greeUser(username):
	# 显示简单的问候语
	print("Hello,"+username.title()+"!")

# greeUser('zhoujielun')

#参数默认值
def describePet(petName, animalType='dog'):
	print("\nI have a "+animalType+".")
	print("My "+animalType+"'s name is "+petName.title()+".")

describePet("sdf")
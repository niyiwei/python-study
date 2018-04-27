#创建和使用类
class Dog(object):
	"""docstring for Dog"""
	def __init__(self, name, age):
		"""初始化属性name和age"""
		self.name = name
		self.age = age

	def sit(self):
		"""模拟小狗被命令时蹲下"""
		print(self.name.title()+" is now sitting.")

	def rollOver(self):
		"""模拟小狗被命令时打滚"""
		print(self.name.title() + " rolled over!")

# __init__ 方法是一个特殊的方法，每当你根据Dog类创建新实例时，Python都会自动运行它。开头和末尾各有两个下划线
#这是一种约定，旨在避免Python默认方法与普通方法名称冲突

myDog = Dog("willie", 6)
print("My dog's name is "+ myDog.name.title()+".")
print("My dog is "+str(myDog.age) + " years old.")

#访问类的属性
myDog.name

#调用方法

myDog.sit()
myDog.rollOver()

print("\n\n\n")

#创建多个实例
yourDog = Dog("luck", 3)
print("Your dog's name is "+ yourDog.name.title()+".")
print("Your dog is "+str(yourDog.age) + " years old.")
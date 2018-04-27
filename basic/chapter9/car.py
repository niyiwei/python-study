class Car():
	""" 一次模拟汽车的简单尝试 """

	def __init__(self, make, model, year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		#给属性默认值
		self.odometerReading = 0

	def getDescriptiveName(self):
		"""返回整洁的描述性信息"""
		result = str(self.year) + ' ' + self.make + ' ' + self.model
		return result.title() 

	def readOdometer(self):
		"""打印一条指出汽车里程的消息"""
		print("This car has " + str(self.odometerReading) + " miles on it.")

	def updateOdometer(self, mileage):
		"""将里程表读数设置为指定的值"""
		self.odometerReading = mileage

	def incrementOdometer(self, miles):
		"""将里程表读数增加指定的量"""
		self.odometerReading += miles

# myNewCar = Car("audi", 'a4', 2016)
# print(myNewCar.getDescriptiveName())
# myNewCar.readOdometer()
# #修改属性的值-直接修改
# myNewCar.odometerReading = 123456
# myNewCar.readOdometer()
# #修改属性的值-通过方法修改
# myNewCar.updateOdometer(666666)
# myNewCar.readOdometer()

# myNewCar.incrementOdometer(111111)
# myNewCar.readOdometer()


#继承
# class ElectricCar(Car):
# 	"""电动汽车的独特之处"""

# 	def __init__(self, make, model, year):
# 		"""初始化父类的属性"""
# 		super().__init__(make, model, year)

# 	def fillGasTank():
# 		print("This car doesn't need a gas tank!")

# 	def getDescriptiveName(self):
# 		"""返回整洁的描述性信息"""
# 		result = str(self.year) + ' ' + self.make + ' ' + self.model + ' Abcd'
# 		return result.title() 
# myTesla = ElectricCar("tesla", 'model s', 2016)
# print(myTesla.getDescriptiveName())


#将实例用作属性
class Battery():
	"""一次模拟电动汽车电瓶的简单尝试"""
	def __init__(self, batterySize=70):
		self.batterySize = batterySize

	def describeBattery(self):
		"""打印一条描述电瓶容量的消息"""
		print("This car has a " + str(self.batterySize) + "-KWh battery.")

class ElectricCar(Car):
	"""docstring for ElectricCar"""
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()

# myTesla = ElectricCar('tesla', 'model s', 2016)
# print(myTesla.getDescriptiveName())
# myTesla.battery.describeBattery()
		

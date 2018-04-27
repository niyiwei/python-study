#从一个模块中导入一个类
from car import ElectricCar
myTesla = ElectricCar('tesla', 'model s', 20161)
print(myTesla.getDescriptiveName())
myTesla.battery.describeBattery();
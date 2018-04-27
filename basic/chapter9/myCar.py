#导入单个类
# from car import Car
#导入多个类
#from car import Car, ElectricCar

# myNewCar = Car('audi', 'a4', 2016)
# print(myNewCar.getDescriptiveName())


# myNewCar.odometerReading = 23;
# myNewCar.readOdometer();

# myTesla = ElectricCar('tesla', 'roadster', 2016)
# print(myTesla.getDescriptiveName())

#导入整个模块
import car;
myBettle = car.Car("volkswagen", 'bettle', 2016)
print(myBettle.getDescriptiveName())

myTesla = car.ElectricCar('tesla', 'roadster', 2016)
print(myTesla.getDescriptiveName())
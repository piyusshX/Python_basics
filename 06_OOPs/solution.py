class Car:
    total_car = 0
    # self is same as this in Js
    def __init__(self, brand, model): # __init__ -> constructor in Python
        self.__brand = brand # We can make a varible private by using __ in front of it
        self.__model = model 
        Car.total_car += 1

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self): # Polymorphism
        return "Petrol or Diesel"

    @staticmethod
    def general_desc(): # static method / decorators -> Accessable by class but not its instance
        return "Its a diesel car"

    @property # it made the model method as attribute
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self): # Polymorphism
        return "Electric Charge"

my_car = Car("BMW", "GT-60")
# print(my_car.__brand) # cannot access private variables
# print(my_car.__model)

new_car = Car("Tata", "Safari")
# new_car.model = "Nexis"
# print(new_car.model)
# print(new_car.full_name())

# print(Car.total_car)

tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(tesla.full_name())

# print(Car.general_desc())

print(isinstance(tesla, Car)) # True
print(isinstance(tesla, ElectricCar)) # True


class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

new_tesla = ElectricCarTwo("Tesla", "Model S")

print(new_tesla.battery_info())
print(new_tesla.engine_info())
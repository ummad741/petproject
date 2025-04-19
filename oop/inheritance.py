# what is inheraitance bu meros olish parrnedan childga
# yani child parentdegi eventlarni oziga kochirib qoshim function qosha olad
# shunda parent ichki arhitekturasi bizilib ketimidi
# child osha arhitekuraga update qosha oladi

# types of inheritance
# 1 single inhrt

# single inhrt -> see it here images/single_inhrt.png
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')

# Child class


class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')


# Create object of Car
car = Car()

# access Vehicle's info using car object
car.Vehicle_info()
car.car_info()

# multiple inhrt -> see it here images/multiple_inhrt.png

# Parent class


class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)

# Parent class 2


class Company:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)

# Child class


class Employee(Person, Company):
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)


# Create object of Employee
emp = Employee()


# access data
emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.Employee_info(12000, 'Machine Learning')

# object


class Getter:
    def get_items(*args):
        print(args)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location


class Employee(Person, Company):
    def __init__(self, name, age, company_name, location, salary, skill):
        super().__init__(name, age)
        super().__init__(company_name, location)
        self.salary = salary
        self.skill = skill

    def show(self):
        print()


emp = Employee('Jessa', 28, 'Google', 'Atlanta', 12000, 'Machine Learning')
print(emp.company_name)

getter = Getter()
# getter.get_items(emp.age, emp.salary, emp.company_name)

# multi level inhrt -> see it here images/multilevel.png


class Head:
    def __init__(self, face):
        self.face = face


class Body(Head):
    def __init__(self, face, press):
        super().__init__(face)
        self.press = press


class Human(Body):
    def __init__(self, face, press):
        super().__init__(face, press)

        print(self.face, self.press)


# Hierarchical Inheritance  -> see it here images/hierarchical.png

class Vehicle:
    def info(self):
        print("This is Vehicle")


class Car(Vehicle):
    def car_info(self, name):
        print("Car name is:", name)


class Truck(Vehicle):
    def truck_info(self, name):
        print("Truck name is:", name)


obj1 = Car()
obj1.info()
obj1.car_info('BMW')

obj2 = Truck()
obj2.info()
obj2.truck_info('Ford')

# hybrid inhrt -> see it here images/hybrid.png


class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle class")


class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")


class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")

# Sports Car can inherits properties of Vehicle and Car


class SportsCar(Car, Vehicle):
    def sports_car_info(self):
        print("Inside SportsCar class")


# create object
s_car = SportsCar()

s_car.vehicle_info()
s_car.car_info()
s_car.sports_car_info()
# class method
# class method faqat class variablar bilan ishlidi instance variablelarga acces olomidi
from datetime import date


class Student:
    school_name = "ABC-School"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def updater(cls, name):
        cls.school_name = name

    @classmethod
    def calculate_age(cls, birth_year: int):
        return date.today().year - birth_year

    @classmethod
    def create_object_via_classmethod(cls, name, birth_year: int):
        # bu classni ozi yani __init__ chaqiriladi
        # cls __init__ atributelarini olib unga add qiladi
        return cls(name, date.today().year - birth_year)


student0 = Student('steave', 20)
print(student0.school_name)
student0.updater('28-maktab')
print(student0.school_name)
print(student0.calculate_age(1900))
print(student0.__dict__)
student1 = Student.create_object_via_classmethod('alisa', 2000)
print(student1.__dict__)


class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_price(cls, name, price):
        return cls(name, (price * 85))

    def show(self):
        print(self.name, self.price)


class Car(Vehicle):
    pass


bmw_usa = Car("BMW X5", 65000)  # use cost of bmw
bmw_usa.show()

bmw_ind = Car.from_price("BMW X5", 65000)  # indian cost of bmw
bmw_ind.show()


# static method
# classga bogliq bomagan lekin class ichidagi yordamchi method hisoblanadi
class Person:
    def __init__(self, name: str, birth_year: int):
        self.name = name
        self.birth_year = birth_year
        self.age = self.calculate_age_and_validate(self.birth_year)

    # matematik amalar validation,fayl formatlash uchun ishlatiladi

    @staticmethod
    def calculate_age_and_validate(birth_year):
        today = date.today().year
        if today < birth_year:
            raise ValueError(
                "Error: Tug‘ilgan yil hozirgi yildan katta bo‘lishi mumkin emas.")

        return today - birth_year

    def show_info(self):
        print(self.name, self.age, self.birth_year)


p1 = Person('jacob', 3900)
p1.show_info()

class Employee(object):

    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name

    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        return requirement

    # instance method
    def work(self):
        # call static method from instance method
        requirement = self.gather_requirement(self.project_name)
        for task in requirement:
            print('Completed', task)

emp = Employee('Kelly', 12000, 'ABC Project')
emp.work()

# Call Static Method from Another Method
class Test :
    @staticmethod
    def static_method_1():
        print('static method 1')

    @staticmethod
    def static_method_2() :
        Test.static_method_1()

    @classmethod
    def class_method_1(cls) :
        cls.static_method_2()

# call class method
Test.class_method_1()
# __call__

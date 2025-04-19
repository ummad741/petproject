# instance variables

# object yani inctance yaratilganda oziga hos bolgan ozgaruvchilar
# har bir objectni oziga hos instance ozgaruvchilari bo'ladi

# objectga tegishli malumot qabul qiladi


class Student:
    def __init__(self, name, age):
        self.name = name  # see it here images/instance_variable.png
        self.age = age

# jacob objectida faqat jacobga tegishli data bor
# lekin shablon bitta yani class


# first object
jacob = Student('jacob', 18)
print('Object 1')
print('Name:', jacob.name)  # har bir objectning values ozi mos
print('Age:', jacob.age)
# second object
sarra = Student('sarra', 18)
print('Object 1')
print('Name:', sarra.name)  # har bir objectning values ozi mos
print('Age:', sarra.age)

# modify values of instance
sarra.name = "qarga"
jacob.age = 30


# way to access instance variable

class StudentAccessAddDel:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # first way via instance method

    def show(self):
        print(self.name, self.age)


# second way
s1 = StudentAccessAddDel('test', 20)
print('Name:', getattr(s1, 'name'))
print('Age:', getattr(s1, 'age'))

# dynamic adding instance variable to object
s1.marks = 70
print('Name:', s1.name, 'Age:', s1.age, 'Marks:', s1.marks)

# list all instance variables
print(s1.__dict__, '---')
for key, value in s1.__dict__.items():
    print(f"{key} = {value}")
    # dynamic deleting instance variable to object
del s1.name  # first way
delattr(s1, 'marks')  # second way
print(s1.name)


class Vehicle:
    def __init__(self):
        self.engine = '1500cc'


class Car(Vehicle):
    def __init__(self, max_speed):
        # call parent class constructor
        super().__init__()
        self.max_speed = max_speed

    def display(self):
        # access parent class instance variables 'engine'
        print("Engine:", self.engine)
        print("Max Speed:", self.max_speed)


# Object of car
car = Car(240)
car.display()

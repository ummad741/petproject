# constructor advansed

class Student:
    # constructor created with the class when its created

    def __init__(self, name, age):  # constructor __init__ you can see it here images/constructor.png
        # constructor helping add instance varaibles self.atr
        self.name = name
        self.age = age
        print(self.name, "hello your age is:", self.age)

    # insctance method
    def show(self):
        print(self.name, f"sani yoshin{self.age}")


s1 = Student('Jacob', 10)
s1.show()

# types of constructors you can see it here images/class object

# default constructor
# py file ichida bomidi va avtomatik ravish standart cons beradi class for initialized


class DefaultCons:  # 1  type of cons

    def display(self):  # x = self its mistake
        print("inside display")


default = DefaultCons()
default.display()


class NonCons:  # 2 Non-Paramitrized Cons

    # no arguments constructor
    def __init__(self):
        self.name = "hello"
        self.age = 20

    # instance method
    def show(self):
        print(f'name:{self.name}, age:{self.age}')


NonCons().show()
variable = NonCons()
print(variable.show())


class ParamsCons:  # Paramitrized constructor

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_data(self):
        print(f"{self.name}, {self.age}")


human1 = ParamsCons('Jarvis', 20)
human2 = ParamsCons('Alisa', 18)

# ParamsCons.show_data() # there have not value i.e object
human1.show_data()
human2.show_data()


class Human:
    # constructor with default values
    def __init__(self, press, hand=2, head=1, leg=2):

        self.press = press
        self.hand = hand
        self.head = head
        self.leg = leg

    def show_data(self):
        print(f"{self.press}")

# test = Human(6)
# test2 = Human(3,3)
# print(test.hand,test.press)


# counting object
class Employee:
    count = 0

    def __init__(self):
        Employee.count = Employee.count + 1


# creating objects
e1 = Employee()
e2 = Employee()
e3 = Employee()
print("The number of Employee:", e3.count)

# Constructor Chaining

# its mistake  thinking
# class HeadDetails:
#     def __init__(self, hair, eye, face, ear, mouth, Nose):
#         self.hair = 'few'
#         self.eye = 2
#         self.face = 1
#         self.mouth = 1


# Head (Parent)
#    ↓
# Body (Child of Head)
#    ↓
# Human (Child of Body, Grandchild of Head)d

class Head:
    def __init__(self, hair, eye, face, ear, mouth, nose):  # for example
        self.hair = hair
        self.eye = eye
        self.face = face
        self.ear = ear
        self.mouth = mouth
        self.nose = nose


class Body(Head):
    def __init__(self, hair, eye, face, ear, mouth, nose, legs, hands, press):  # for example
        super().__init__(hair, eye, face, ear, mouth, nose)
        self.legs = legs
        self.hands = hands
        self.press = press


class Human(Body):  # last
    def __init__(self, hair, eye, face, ear, mouth, nose, legs, hands, press, beautiful):
        super().__init__(hair, eye, face, ear, mouth, nose, legs, hands, press)
        self.beautiful = beautiful

    def __str__(self):
        return (f"Human(hair={self.hair}, eye={self.eye}, face={self.face}, ear={self.ear}, "
                f"mouth={self.mouth}, nose={self.nose}, legs={self.legs}, hands={self.hands}, "
                f"press={self.press}, beautiful={self.beautiful})")


jacob = Human('black', 'brown', 1, 1, 2, 'small', 2, 2, 6, True)
print(jacob)

# ----IHERITANCE----
# Head (Parent)
#    ↓
# Body (Child of Head)
#    ↓
# Human (Child of Body, Grandchild of Head)


print(Human.__mro__)  # MRO Method Resolution Order

# what is incopsulation(incopsulatsiya) ->
# see it here  images/incopsulation.png

# Encapsulation is a method of hiding the internal state (data/properties) of an object (class)
# from external interference and allowing access only through necessary functions (methods).
# 🧠 That is: "Protecting the information inside" and controlling how it can be changed.

# incopsulatsiya data properties class yoki obkject ichidagi data yani malumotni
# izalyatsiya qilish tashqi ozgarishdan himoya qilish
# va himoyalangan datani uni qanaqa ozgartirishi nazorat qilish

# faqat kereli function yoki methodlari bilan foydalanishga ruxsat berish usuli

# benefit(foydasi)
# 1 data/protection(malumotlar hafvsizligi)
# 2 protecting incorrect changes(datani notogri ozgartirishlardan himoya)
# 3 strict control in system(tizimda qatiq nazorat qoyish


# 3 types of modifiers(uch xil modifierlar)
# 1 public member(ochiq)
# 2 protect member(himoyalanga) -> _atr
# 3 private member(yopiq) -> __atr

class TypesofMembers:
    def __init__(self, name, age, point, salary):
        # public member
        self.name = name
        self.age = age
        # protect member
        self._point = point
        # private member
        self.__salary = salary

    def show(self):
        print(f'name:{self.name}, age:{self.age}')


class Company:
    def __init__(self):
        # protect member
        self._project = "NLP"

# super().__init__ ✅  dynamic, MRO
# Company.__init__ ❌  static, bad experience


class Employee(Company):
    # constructor
    def __init__(self, name, salary):
        super().__init__()  # companyda argument berilmagan
        # public data member
        self.name = name
        # private member
        self.__salary = salary

    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)
        # Accessing protected member in child class
        print(f'protect_data: {self._project}')

    # getter method

    def getter(self):  # getter
        return self.__salary

    # setter method
    def setter(self, money):  # simple check
        if money != self.__salary:
            print(f"stolen money bigger or less than {self.__salary}")

        self.__salary = money
        print("has been paid:", self.__salary)


emp = Employee('Jessa', 10000)
# getter
print(emp.getter())
# setter
emp.setter(10000)

# accessing private data members
# correct way to accessing to private data member
print("Salary:", emp._Employee__salary)  # first solution
emp.show()  # second solution
# print('Salary:', emp.__salary)  # incorrect way to accessing

# Decarator(codeni ozgartirmastan unga qoshimcha function qoshish) -> @
# for example
def decarator_function(original_function):
    def wrapper_function():
        print("decarator working!")
        original_function()

    return wrapper_function


@decarator_function
def say_hello():
    print('hello world')


say_hello()

class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) >= 3:
            self.__name = new_name
        else:
            print("Ism juda qisqa!")

s1 = Student("Jacob")
print(s1.name)      # Getter
s1.name = "Al"      # Setter ishga tushadi
print(s1.name)


# what is poliymorphism ->
# Poliymorpthism(bu method bitta method bir nechta shaklda ishlashi mumkun degani)

# "Polymorphism" — bu bitta metod, bir nechta shaklda ishlashi degani.

# Masalan:
# Har xil hayvonlar bor: Dog, Cat, Bird
# Har biri make_sound() degan metodga ega.
# Lekin har bir hayvon o‘z ovozini chiqaradi. Ya'ni, metod nomi bitta, ammo har xil natija beradi.


class Sounds:
    def make_sound(self):
        pass


class Dog(Sounds):
    def make_sound(self):
        print("woof")
        # return super().make_sound()


class Cat(Sounds):
    def make_sound(self):
        print("meow")
        # return super().make_sound()


class Cow(Sounds):
    def make_sound(self):
        print("mooo")
        # return super().make_sound()


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.make_sound())


def add(x, y):
    return x + y

# simple polymarphism len()

string = 'hello world'
tuple_test = (1, 2, 3, 4)
list_test = [1, 2, 3, 4]
# len bu yerda polymorphism chunki bitta functino kop shakilda ishlavoti tuple,list,str 
# len vazifasi olcham 
print(len(list_test)) 
print(len(string))
print(len(tuple_test))



class Ferrari:
    def fuel_type(self):
        print("Petrol")

    def max_speed(self):
        print("Max speed 350")

class BMW:
    def fuel_type(self):
        print("Diesel")

    def max_speed(self):
        print("Max speed is 240")

# normal function
def car_details(obj):
    obj.fuel_type()
    obj.max_speed()

ferrari = Ferrari()
bmw = BMW()

car_details(ferrari)
car_details(bmw)
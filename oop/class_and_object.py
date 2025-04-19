# what is the class = shablon > atributs and functions(methods)
# what is the object this is real thing based on class

# real analogiya for class
# class(retsept) bu retsept 
# object(this is recibased dish) retsept asosida tayorlangan taom


class Mashina:

    # class variable outside of methods in class
    wheels = 4  # like default
    # bolishi kerak bolgan detalar
    # self first detal of object and self its object

    def __init__(self, model, color):  # atributs, states
        # instance belongs to the one object
        self.model = model  # instance variable
        self.color = color  # instance variable

    # behavior yani functioni qiladiga ishi method
    def drive(self):
        print(f'{self.color}, {self.model} is moving')

    # class atributs  you can see it here images/atributs_of_class.png
    # __init__ constructor calling automaticaly
    # self key, expresses itself(working in class)


malibu = Mashina('Malibu', 'oq')
nexia = Mashina('Nexia', 'Chocolate')
spark = Mashina('Spark', 'oq')

print(f"{malibu.model}, {malibu.color}")
print(f"{spark.model}, {spark.color}")
print(malibu.wheels, spark.wheels)  # same result 4
#  start exersizes with learning

# what is tuple you can see here images/tuple_teoriya.png

def exer_1():
    # Reverse the tuple
    tuple1 = (10, 20, 30, 40, 50)

    # first solution
    print(tuple1[::-1])
    # second solution
    print(tuple(reversed(tuple1)))


# exer_1()

def exer_2():
    # Access value 20 from the tuple
    tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

    print(tuple1[1][1])  # access value

# exer_2()


def exer_3():
    tuple1 = (10, 20, 30, 40)
    print(tuple1[0])  # should print 10
    print(tuple1[1])  # should print 20
    print(tuple1[2])  # should print 30
    print(tuple1[3])  # should print 40

# exer_3()


def exer_4():
    tuple1 = (11, 22)
    tuple2 = (99, 88)
    tuple1, tuple2 = tuple2, tuple1
    print(tuple2)
    print(tuple1)


exer_4()


def exer_5():
    # Copy specific elements from one tuple to a new tuple
    tuple1 = (11, 22, 33, 44, 55, 66)
    tuple2 = tuple1[3:-1]
    print(tuple2)


exer_5()


def exer_6():
    # To create a tuple with a single item, you need to add a comma after the item. 
    # Otherwise, Python will not recognize the variable as a tuple, and it will treat it as a string type.
    tuple1 = (11, [222, 33], 44, 55)
    tuple1[2] = 'dalban' # ichida list bogani uchun qoshilgan

    print(tuple1)


exer_6()


def exer_7():
    # Sort a tuple of tuples by 2nd item
    tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
    tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))    
    # print(tuple1)


exer_7()


def exer_8():
    tuple1 = (50, 10, 60, 70, 50)
    print(tuple1.count(50))


exer_8()

# To create a tuple with a single item, you need to add a comma after the item. 
# Otherwise, Python will not recognize the variable as a tuple, and it will treat it as a string type.

def exer_9():
    tuple1 = (4, 45, 45, 45)

    def check(tpl):
        return all(i == tpl[0] for i in tpl)
    
    print(check(tuple1))
        
# exer_9()
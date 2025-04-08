#  start exersizes with learning

# what is tuple you can see here images/set_teoriya.png

def exer_1():
    # set takes unique items and unordered 
    sample_set = {"Yellow", "Orange", "Black"}
    sample_list = ["Blue", "Green", "Red"]

    sample_set.add("Yellow")

    print(sample_set)

# exer_1()

def exer_2():
    # intercsection method taking repeated items
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    # first solution
    print(set1.intersection(set2))

    # second result 
    result =  set1 & set2
exer_2()

def exer_3():
    # takes unqiue items
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    
    # first solution
    print(set1.union(set2))
    # second solution 
    print(set1 | set2)


# exer_3()


def exer_4():
    set1 = {10, 20, 30}
    set2 = {20, 40, 50}
    
    # first solution 
    set1.difference_update(set2)
    
    # second solution
    print(set1)

exer_4()

def exer_5():
    # Return a set of elements present in Set A or B, but not both
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}

    print(set1.symmetric_difference(set2)) # gets only unique items from both set 

exer_5()

def exer_6():
    set1 = {10, 20, 30, 40, 50}
    set2 = {60, 70, 80, 90, 10}

    if set1.isdisjoint(set2):
        print('same items havnt')
    else:
        print(set1 & set2)

exer_6()

def exer_7():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set1.intersection_update(set2)
    print(set1)

exer_7()
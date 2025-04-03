# what is list see it here images/teoriya_list.png

# start exersizes with learning 
def exer_1():
    # reversed list()
    # indexing see it here images/indexing_list.png
    list1 = [100, 200, 300, 400, 500]
    # first solution
    print(list1[::-1])
    # second solution
    result = list(reversed(list1))
    print(result)
    # third solution
    list1.reverse()
    print(list1)


# exer_1()


def exer_2():
    # Concatenate two lists index-wise
    list1 = ["M", "na", "i", "Ke", 'te', 'st']
    list2 = ["y", "me", "s", "lly"]
    result = []

    # first solution real solution
    for first, second in zip(list1, list2):
        result.append(first+second)
    print('real solution:', result)

    # second solution and there have little changes
    l1_len = len(list1)
    l2_len = len(list2)
    length = l1_len if l1_len > l2_len else l2_len
    print(length)
    second_result = []

    for i in range(length):

        if i < l1_len and i < l2_len:

            second_result.append(list1[i]+list2[i])
            continue

        if l1_len > l2_len:
            print(i)
            second_result.append(list1[i])
        else:
            second_result.append(list2[i])

        # not working this code
        # if i < l1_len:
        #     print(i)
        #     second_result.append(list1[i])
        # if i < l2_len:
        #     second_result.append(list2[i])

    print(second_result)


# exer_2()

def exer_3():
    # Turn every item of a list into its square

    numbers = [1, 2, 3, 4, 5, 6, 7]
    result = []
    for num in numbers:
        result.append(num * num)
    print(result)

# exer_3()


def exer_4():
    # Concatenate two lists in the following order
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    result = []

    # simple neested loop
    for i in list1:
        for j in list2:
            result.append(i+j)

    # one line neested loop
    res = [outer + inner for outer in list1 for inner in list2]

    print(res)
    print(result)


# exer_4()

def exer_5():
    # Iterate both lists simultaneously
    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]

    for frst_i, sec_i in zip(list1, reversed(list2)):
        print(frst_i, sec_i)

# exer_5()


def exer_6():
    # remove empty strings
    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    result = list(filter(None, list1))
    print(result)


exer_6()

def exer_7():
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

    list1[2][2].append(7000)

    print(list1)

# exer_7()


def exer_8():
    # Extend nested list by adding the sublist
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

    # sub list to add
    sub_list = ["h", "i", "j"]
    list1[2][1][2].extend(sub_list)
    print(list1)

    my_list = list([5, 8, 'Tom', 7.50])

    # Using insert()
    # insert 25 at position 2
    my_list.insert(2, 25)
    print(my_list)
    # Output [5, 8, 25, 'Tom', 7.5]


# exer_8()

def exer_9():
    # Replace list’s item with new value if found 
    list1 = [5, 10, 15, 20, 25, 50, 20]

    index = list1.index(20)
    list1[index] = 200
    print(list1)


# exer_9()

def exer_10():
    list1 = [5, 20, 15, 20, 25, 50, 20]
    # first solution
    def remove_value(sample, val):
        return [i for i in sample if i != val]
        
    res = remove_value(list1, 20)
    print(res)


    # second solution
    while 20 in list1:
        list1.remove(20)


    print(list1)

# exer_10()
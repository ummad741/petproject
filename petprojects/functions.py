# start exersizes with learning
def exer_1(name, age, default=10):  # see it here images/typesofarguments
    print(name, age)


# exer_1('name', age=10)


def exer2(*args):
    for i in args:
        print(i)

# exer2(20,30,40)


def exer_3(a, b):
    # addition and substraction
    return a + b, a - b


# res = exer_3(50, 10)
# print(res)


def exer_4(name, salary=9000):
    print(f'name:{name} salary:{salary}')


# exer_4("Ben", 12000)
# exer_4("test")


def exer_5(number):
    # sum of number
    def find_sum(number):
        res = 0
        for i in range(number+1):
            res += i
        return res

    sum_of_num = find_sum(number)
    return sum_of_num


# result = exer_5(10)
# print(result)


def exer_6(name, age):
    print(name, age)


shows = exer_6
shows('emma', 18)


def exer_7():
    generator = [i for i in range(0, 30, 2)]
    print(generator)
# exer_7()


def exer_8():
    # Exercise 9: Find the largest item from a given list
    x = [4, 6, 8, 24, 12, 2]
    print(max(x))


exer_8()


def advansed_lambda():
    # simple lambda
    adding = lambda x,y: x + y
    print(adding(5, 5))

    num_list = [10, 5, 12, 78, 6, 1, 7, 9]

    result = list(filter(lambda x: x % 2 == 0, num_list))
    print(result)



advansed_lambda()

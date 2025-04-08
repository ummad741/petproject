def numoutput(a, b) -> int:

    pre_num = 0

    for i in range(10):
        x_sum = pre_num + i
        print(f"Current num :{i} Previous num {pre_num},Sum {x_sum}")
        pre_num = i


# print(numoutput(20,30))


def work_w_string():
    word = input('Enter word: ')

    # i should slice from word via how much
    # how_much = int(input("enter the number: "))
    # print(word[how_much:])

    print("Original String:", word)

    # show even and odd index word
    # stop: size-1 because index starts with 0
    for i in range(0, len(word), 1):
        print(f"[{i}]", word[i])

# work_w_string()


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]


def compare_numbers_first_last(num_list):
    print("list:", num_list)
    if num_list[0] != num_list[-1]:
        return "Result is False"

    return "Result is True "

# print(compare_numbers_first_last(numbers_x))
# print(compare_numbers_first_last(numbers_y))


num_5 = [10, 20, 33, 46, 55]


def divisible_by5(num_list):
    print(f"given: {num_list}")

    for num in num_list:
        if num % 5 == 0:
            print(num)

    # this variant is not true solution
    # cnt_list = len(num_list)
    # print(cnt_list)

    # div_list = []
    # for i in range(0,cnt_list,1):
    #     div_list.append(num_list[i] % 5 == 0)

    # return div_list


# print(divisible_by5(num_5))

sentence = "Emma is good developer. Emma is a writer"


def count_substr(stnce):

    sub_str = input("enter the word: ")
    if sub_str not in stnce:
        return "no such word in the sentence"

    count_substr = stnce.count(sub_str)

    return f"{sub_str} appeared {count_substr}"


# print(count_substr(sentence))


# following pattern
def following_pattern():
    for num in range(5):
        # print('a')
        for i in range(num):
            # print(i)
            print('b', num, end='')
        # print('\n')

# following_pattern()


# number = int(input("enter the number: "))


def palindrom_num(num):
    num_str = str(num)
    reversed_num = num_str[::-1]

    return num_str == reversed_num

# if palindrom_num(number):
#     print("palindrom num")
# else:
#     print("not palindrom num")


def merging_list():
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5]

    result_list = []

    for nums in list1:
        if nums % 2 != 0:
            result_list.append(nums)

    for nums in list2:
        if nums % 2 == 0:
            result_list.append(nums)

    print(result_list)

# merging_list()


# def reverse_number():
# number = int(input("enter the number: "))

# print(int(str(number)[::-1]))


def multiplication():

    for nums in range(1, 11):
        print('outer', nums)
        for i in range(1, 11):
            print(nums * i, end=' ')


# multiplication()


def pyramid():
    for i in range(5, 0, -2):
        print(i)
        for j in range(i):
            print('*', end=' ')
        print(' ')


pyramid()


base = 5
exponent = 4
result = base ** exponent

# print (f"{base} raises to the power of {exponent}: {result} i.e. ")


def exponent(base, exp):
    num = exp
    result = 1
    # num less than 0 cycle is stoped
    while num > 0:
        result = result * base
        print(result)
        num = num - 1
        print(num)
    print(base, "raises to the power of", exp, "is: ", result)


# exponent(5, 4)

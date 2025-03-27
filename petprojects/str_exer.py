# 1 exer a
def middle_str():
    str1 = 'qwertyuiopasdfghjklzxcvbnmaaaaaa'

    print(len(str1))
    middle = int(len(str1) / 2)

    print(middle)
    print(str1[middle])
    # i need to show first middle last character in given str
    # if length of word shows the middle 2 words
    if len(str1) % 2 == 0:
        print(str1[0]+str1[middle:middle+2]+str1[-1])
    else:
        print(str1[0]+str1[middle]+str1[-1])

    # 1 exer b

    str2 = "JaSonAy"

    middle2 = int(len(str2) / 2)
    print(middle2)

    print(str2[middle2-1:middle2+2])


# 2 exer
def exer2():
    s1 = "Ault"
    s2 = "Kelly"

    middle = int(len(s1) / 2)
    print(middle)

    print(s1[:middle]+s2+s1[middle:])


def exer3():
    s1 = "America"
    s2 = "Japan"
    middle = int(len(s1) / 2)
    middle2 = int(len(s2) / 2)

    print(s1[0]+s2[0]+s1[middle]+s2[middle2]+s1[-1]+s2[-1])


def exer4():
    string1 = "PyNaTive"
    lower = []
    upper = []

    # simple result
    print(len(string1))
    for i in string1:
        if i.islower():
            lower.append(i)
        else:
            upper.append(i)

    result = ''.join(lower+upper)
    print(result)

    # reverse result
    # for i in range(len(string1), 0, -1):
    #     if string1[i-1].islower():
    #         lower.append(string1[i-1])
    #     else:
    #         upper.append(string1[i-1])

    # print(lower, upper)
    # reverse_result = ''.join(lower+upper)
    # print(reverse_result)


# exer4()

def exer5():
    # divide into groups and count each characters,symbols and digits
    string = "P@#yn26at^&i5ve"
    print(string.isalpha())

    chars = []
    digits = []
    symbols = []

    for i in string:

        if i.isalpha():
            chars.append(i)
        elif i.isdigit():
            digits.append(i)
        else:
            symbols.append(i)
    print(f"chars:{len(chars)}, digits:{len(digits)}, symbols:{len(symbols)}")


def exer_6():
    s1 = "Abc"
    s2 = "Xyza"
    res = ''
    # # its my solution there have any bugs solutions is static
    # for first, second in zip(s1, s2[::-1]):

    #     res += first + second

    # print(res)

    # second solutions is dynamic
    s1_length = len(s1)
    s2_length = len(s2)
    print(s1_length, s2_length)
    # takes bigger length
    lenght = s1_length if s1_length > s2_length else s2_length
    s2 = s2[::-1]
    result = ''
    for i in range(lenght):
        print(i)
        # ohirgisida qaysi biri kota bosa oshani harifini qowvoradi
        if i < s1_length:
            result += s1[i]
        if i < s2_length:
            result += s2[i]
    print(result)


# exer_6()


def exer_7():
    str1 = "Welcome to USA. usa awesome, isn't it?"

    lower = str1.lower()
    print(lower.count("usa"))


# exer_7()


def exer_8():
    str1 = "PYnative29@#8496"
    total = 0
    cnt = 0

    # pre_num = 0
    # test = []

    # for i in range (len(str1)):
    #     if str1[i].isdigit() :

    #         test.append(str1[pre_num]+str1[i])
    #         pre_num = i
    # print(test)

    for char in str1:

        if char.isdigit():
            print(char)
            total += int(char)
            # print(total)
            cnt += 1

    avg = total / cnt
    print("Sum is:", total, "Average is ", avg)

# exer_8()


def exer_9():
    exmpl = "Apple"
    my_dict = {}

    for i in exmpl:

        my_dict[i] = exmpl.count(i)

    print(my_dict)


# exer_9()


def exer_10():
    # i need to reverse
    string_exer = "PYnative"

    print(string_exer[::-1])

    # second solution
    str1 = ''.join(reversed(string_exer))
    print("Reversed String is:", str1)


# exer_10()

def exer_11():
    str1 = "Emma is a data scientist who knows Python. Emma works at google."

    # find the last Emma index

    print(str1.rfind("Emma"))  # reverse find
# exer_11()


def exer_12():

    str1 = " Emma-is-a-data-scientist"

    str1 = str1.split('-')
    print(str1)


# exer_12()


def exer_13():
    str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
    res_list = []

    # first solution
    for i in str_list:
        if i:
            res_list.append(i)

    result = list(filter(None, str_list))
    print(result)

    # second solution
    print(res_list)


# exer_13()

def exer_14():
    str1 = 'I am 25 years and 10 months old'

    result = ''.join(i for i in str1 if i.isdigit())
    print(result)

# exer_14()


def exer_15():
    str1 = "Emma25 is Data scientist50 and AI Expert"

    temp = str1.split()

    result = []
    for item in temp:

        if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
            result.append(item)

    # agar variablega tenglamasa objectni ochib beromidi
    for i in result:
        print(i)


exer_15()

def exer_16():
    str1 = '/*Jon is @developer & musician!!'


    for i in str1:
        if not i.isdigit() and not i.isalpha():
            str1 = str1.replace(i, '#')

    print(str1) 

    for char in string.punctuation:
        str1 = str1.replace(char, replace_char)
exer_16()

        
        

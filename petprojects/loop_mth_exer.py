
# for looooooooooooooooooop ?!?!
def exer_1():
    for i in range(10):
        print(i)

# exer_1()


def exer_2():

    # nested loop
    for i in range(1, 7):  # outer loop
        print(i)
        for j in range(1, i):  # inner loop
            print(j, end='')
        print('')

# exer_2()


def exer_3_and_4():

    a = 0

    inp = int(input('enter the number: '))
    # second solution
    result = sum(range(1, inp+1))
    print(result)
    # first solution  55 (1+2+3+4+5+6+7+8+9+10)
    for i in range(inp+1):
        a += i
    print(a)

    # exer_4
    num = 2
    for i in range(inp+1):
        print(num * i)
# exer_3_and_4()


def exer_5():
    # Write a Python program to display only those numbers from a list that satisfy the following conditions

    # The number must be divisible by five
    # If the number is greater than 150, then skip it and move to the following number
    # If the number is greater than 500, then stop the loop

    numbers = [12, 75, 150, 180, 145, 525, 50]

    for i in numbers:

        # there have any little little mistake
        # if i % 5 == 0:
        #     if i <= 150:
        #         # print(i)

        # checking each items and compareing
        if i > 500:
            break
        elif i > 150:
            continue
        elif i % 5 == 0:
            print(i)
# exer_5()


def exer_6():
    # Count the total number of digits in a number
    # For example, the number is 75869, so the output should be 5.
    number = 75869
    cnt = 0

    while number != 0:

        number = number // 10  # ohirgi raqami kamaytirib keladi
        print(number)
        cnt += 1
    print(cnt)


# exer_6()

def exer_7():

    # output
    # 5 4 3 2 1
    # 4 3 2 1
    # 3 2 1
    # 2 1
    # 1
    n = 5
    k = 5
    for i in range(0, n+1):
        for j in range(k-i, 0, -1):
            print(j, end=' ')
        print()


# exer_7()

def exer8():
    # Print list in reverse order using a loop

    # first solution
    list1 = [10, 20, 30, 40, 50]
    rev_list = reversed(list1)

    for i in rev_list:
        print(i)
    # second solution
    for i in range(len(list1), 0, -1):
        print(list1[i-1])

# exer8()


def exer_9():
    # reverse start, stop ,step
    for i in range(-10, 0, 1):
        print(i)

    # simple start, stop ,step
    for i in range(0, 11, 1):
        print(i)
# exer_9()


def exer_10():

    for i in range(5):
        print(i)
    else:
        print('done')

# exer_10()


def exer_11():
    # find prime numbers
    start = 25
    end = 50

    for num in range(start, end+1):
        # print(i)

        if num > 1:
            for i in range(2, num):
                # print(j)
                # print(f' outer:{num}, inner{i}')
                if num % i == 0:
                    # not a prime number so break inner loop and
                    # look for next number
                    break
            else:
                print(num)


# exer_11()


def exer_12():
    # fibonachi sequence
    num1 = 0
    num2 = 1
    for i in range(10):

        print(num1)

        res = num1 + num2
        num1 = num2
        num2 = res
# exer_12()


def exer_13():
    # factorial

    pre_num = 1
    test = 1
    for i in reversed(range(1, 6)):
        pre_num *= i
    for i in range(1, 6):
        test *= i

    # second solution there have validations
    # if num < 0:
    #     print("Factorial does not exist for negative numbers")
    # elif num == 0:
    #     print("The factorial of 0 is 1")
    # else:
    #     # run loop 5 times
    #     for i in range(1, num + 1):
    #         # multiply factorial by current number
    #         factorial = factorial * i
    #     print("The factorial of", num, "is", factorial)

    print(test)
    print(pre_num)


# exer_13()

def exer_14():
    # reverse integer number:
    number = 76542
    result = str(number)[::-1]
    # print(int(result))

    num = 76540
    reverse_number = 0
    # print("Given Number ", num)
    while num > 0:
        reminder = num % 10
        # print(reminder)

        reverse_number = (reverse_number * 10) + reminder
        # print(reverse_number)
        # print(reverse_number*10)

        num = num // 10  # bu bitta bitta songa kamaytirib turibdi
    print(reverse_number)

# exer_14()


def exer_15():

    # list slicing
    # variant 1 
    my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for i in range(len(my_list)):

        if i % 2 == 0:
            print(i)
            print(my_list[i])

    # stat from index 1 with step 2( means 1, 3, 5, an so on)
    # variant 2
    for i in my_list[0::2]:
        print(i, end=" ")


# exer_15()

def exer_16():
    # find cube number
    inp = int(input('enter the number: '))
    for i in range(inp+1):

        print(f"Current Number is : {i}  and the cube is {i*i*i}")

exer_16()
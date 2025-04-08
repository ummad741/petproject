# start exersizes with learning 
def exer_1():

    number = int(input('Enter any number between 100 and 500 '))
    # number greater than 100 and less than 500
    while number < 100 or number > 500:
        print('Incorrect number, Please enter correct number:')
        number = int(input('Enter a Number between 100 and 500 '))
    else:
        print("Given Number is correct", number)

# exer_1()


def exer_2():

    infiniti = True
    while infiniti:
        print('hello')
        # infiniti = False


# exer_2()

def exer_3():

    name = 'Jesaa29Roy'
    size = len(name)
    iterate_num = 0
    # iterate loop till the last character
    while iterate_num < size:
        # break loop if current character is number
        # diferent exer and solution
        if name[iterate_num].isdecimal():
            iterate_num += 1
            continue

        # real solution
        # if name[i].isdecimal():
        #     break

            # print current character

        print(name[iterate_num], end=' ')
        iterate_num += 1


# exer_3()


def exer_4():
    iterate_num = 1
    # outer while loop
    # 4 rows in pattern
    while iterate_num < 5:  # outer
        j = 0
        # nested while loop
        while j < iterate_num:  # inner
            print('*', end=' ')
            j = j + 1
        # end of nested while loop
        # new line after each row
        print('')
        iterate_num = iterate_num + 1


def exer_5():
    # reverse while loop
    iterate_num = 10
    while iterate_num >= 0:
        print(iterate_num, end=' ')
        iterate_num = iterate_num - 1

# exer_5()


def exer_6():
    # iterate string
    string = "jessa"
    lenght = len(string)
    iterate_num = 0
    while iterate_num < lenght: # when itr_num equal length while stops
        
        print(string[iterate_num])
        iterate_num += 1
        # 
        print(iterate_num)

exer_6()
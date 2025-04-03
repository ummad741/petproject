# first = int(input("enter the first numbers: "))
# second = int(input("enter the second numbers: "))

# print(f'result {first * second}')

# word = input("enter the word: ")

# print('My', 'Name', 'Is', 'James', sep='**')


# for i in range(1)

import os


with open("test_1.txt", 'w') as fp:
    fp.write("")

# file is empty or not
size = os.stat('test_1.txt').st_size == 0
print(size)


x = ('apple', 'banana', 'cherry')

for index, thing in enumerate(x):
    print(index, thing)
    


with open('experience.txt', 'r') as exer:

    # reader =exer.readlines()
    # print(reader)
    line_numbers = [4, 7]
    # print(len(exer))

    lines = []
    # for i in range(1, len(exer)):




    for index, items in enumerate(exer):
        if index in line_numbers:
            lines.append(items.strip())
        elif index > 7 :
            break

    print(lines)

with open('experience.txt', 'r') as idea:
    reader=idea.readlines()
    # start = 0 stop=n  step = 2 bosa odd
    # for i in range(3,len(reader): cuting
    # for i in range(-3,0): reverse cuting

    for i in range(1,len(reader),2):
        print(reader[i])

open()

    



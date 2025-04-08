 # start exersizes with learning 
# with open('docs.txt', 'w') as w_method:
#     pass

# # if alredy exist opened file append new runs code dont clear previous code
# with open('docs.txt', 'a') as a_method:
#     pass


# # if the file already exist gives and error
# # with open('docs.txt', 'x') as x_method :
# #     pass

import os
import shutil
from datetime import datetime

# get current date and time
x = datetime.now()


# file_name_2 = x.strftime('%d-%m-%Y-%H-%M-%S.txt')
# with open(file_name_2, 'a') as fp:
#     print('created', file_name_2)

# shutil.move(file_name_2, 'pyVariables/')


with open('docs.txt', 'w') as w_method:
    person_data = ['Name: Emma',
                   '\nAddress: 221 Baker Street', '\nCity: London']
    # w_method.write(person_data)
    # w_method.writelines(person_data)


new_test = open('experience.txt', 'a')
new_test2 = open('result.txt', 'w')
# new_test.write('something\n')

exer = open('experience.txt', 'r')
lines = exer.readlines()

print(lines)

cnt = 0


for line in lines:
    # print(line)
    # print('bosh', cnt)
    if cnt == 4:
        cnt += 1
        
        continue
    else:
        # print(line)
        new_test2.write(line)

    cnt += 1
    # print(cnt) 




# with open('docs.txt', 'r') as test_seek :
#     test_seek.seek(5)
#     print(test_seek.read())


# os.rename('docs.txt', 'change.txt')
# with open('change.txt', 'r') as file_read:
#     print(file_read.read())
#     file_read.close

# with open('str_exer.py', 'w'):
#     pass
# shutil.move('str_exer.py', 'petprojects/') 
# shutil.copy('change.txt', 'pystring/')
# shutil.move('change.txt', 'pyVariables/')
# os.remove('pyVariables/change.txt')
# os.remove('pystring/change.txt')

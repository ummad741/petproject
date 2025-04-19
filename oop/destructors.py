# what is destructors you can see it here images/destructor.png


# how works destructors see it here images/work_destructors.py

# destructor bu obect ochirgandegi avtomatik ravishda ishga tushadigan method 

# object ochirilganda avtomatik ravishda 
# 1 object resurlarini tozalidi (resurs cleaning)
# 2 file yopish (file close)
# database  aloqani buzish  (destroy the connection from database)

class Filemanager:
    def __init__(self, filename):
        self.file = open(filename,  'a')
        print('file opened for writing')

    def write(self, content):
        self.file.write(content)

    def __del__(self):
        self.file.close()
        print('file closed')


test = Filemanager('test.txt')

test.write('hello')

del test
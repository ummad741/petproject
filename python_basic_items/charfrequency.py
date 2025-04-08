

a = 'google.com google google gg g g g g g h / q'
# hatoyim for tashqarisida dict ochamaganim keyin count alohida

secdict = {}



# for items in a:

#     if items in secdict:
#         # agar a ichidagi item bomasa divomana imena osha elementga 1 qosh divoman
#         secdict[items] +=1
#     else:
#         secdict[items] = 1
# print(secdict)


# solution

def some(str):

    mydict = {}
    
    for n in str:
        # best solution 
        mydict[n] = str.count(n)
   
        # long solution
        keys = mydict.keys()
        if n in keys:
            mydict[n] += 1
        else:
            mydict[n] = 1

    print(mydict)
    return  mydict



print(some(a))

# for items in a:
#     count = 0
#     mydict = {}
#     tekshiruvchi=mydict[items]
#     print(tekshiruvchi)
#     if mydict[items] == items:
#         count += 1
#         mydict[items] = count
#         print(mydict)
#     else:
#         print('qisib tur')


# def char_freequenc(str):

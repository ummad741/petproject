example = "w3ba"


if len(example) > 2 :
    print(f"{example[:2]}{example[-2:]}")
elif len(example) == 2:
    print(f"{example[:2]}{example[-2:]}")
else:
    print('Empty string')

# solution 
def cuting(item):

    if len(item) <2:
        return ''
    
    return item[:2] + item[-2:]
print(cuting(example))
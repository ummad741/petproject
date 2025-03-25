
example = "bc"
example1 = 'abcinging' 


def func(example):

    #first 
    if len(example ) >= 3 :
        if 'ing' not in example:
            example += 'ing'
        else:
            example += 'ly' 


    return example

print(func(example))
print(func(example1))

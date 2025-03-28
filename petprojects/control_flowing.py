# control flowing

def learn_control_flowing():
    # what is control flowing: you can see it here images/control_flowing

    # 1 Transfer statements 

    # example for continue statements you can see it here # images/Continue_statement.png
    numbers = [2, 3, 11, 7] 
    for i in numbers:
        print('Current Number is', i)
        # skip below statement if number is greater than 10
        if i > 10:
            continue # how to work images/Continue.png
        square = i * i
        print('Square of a current number is', square)


    # example for break statements you can see it here images/break_statements.png
    numbers = [10, 40, 120, 230]
    for i in numbers:
        if i > 100:
            break # how to work images/break.png
        print('current number', i)


    #  2 Conditional statements 
    # 3 iterative statements

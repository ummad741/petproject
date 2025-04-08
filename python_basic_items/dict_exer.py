# what is this dictionarly see it here images/teoriya_dict.png


# start exersizes with learning
def exer_1():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    result = {}

    # first solution
    for key, value in zip(keys, values):  # dont takes excess value

        result[key] = value
    print(result)
    # second solution
    result2 = dict(zip(keys, values))  # very simple way
    print(result2)

    # third solution
    for i in range(len(keys)):  # there have any mistakes: IndexError: list index out of range
        result.update({keys[i]: values[i]})
    print(result)


# exer_1()

def exer_2():
    # Merge two Python dictionaries into one
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

    # first solution
    result_dict = {**dict1, **dict2}  # spread unpacking
    print(result_dict)

    # second solution
    dict1.update(dict2)  # simple way
    # print(dict1)

    # third solution
    result_dict = dict1 | dict2  # merge operator
    # print(result_dict)

# exer_2()


def exer_3():
    # Print the value of key ‘history’ from the below dict
    sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }
    # first solution
    print(sampleDict.get('class').get('student').get(
        'marks').get('history'))  # bad way
    # second solution
    print(sampleDict['class']['student']['marks']
          ['history'])  # greater than first way

# exer_3()


def exer_4():
    # Initialize dictionary with default values
    employees = ['Kelly', 'Emma']
    defaults = {"designation": 'Developer', "salary": 8000}

    result = dict.fromkeys(employees, defaults)
    print(result)


# exer_4()

def exer_5():
    # Create a dictionary by extracting the keys from a given dictionary
    sampleDict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"}

    keys = ["name", "salary"]
    print(sampleDict['age'])

    result = {key: sampleDict[key] for key in keys}

    # second solution
    for key in keys:
        result.update({key: sampleDict[key]})
    print(result)


def exer_6():
    # Delete a list of keys from a dictionary
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    # Keys to remove
    keys = ["name", "salary"]

    # # first solution
    sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
    print(sample_dict)

    # second solution
    # for key in keys:
    #     sample_dict.pop(key)
    # print(sample_dict)


# exer_6()

def exer_7():
    sample_dict = {'a': 100, 'b': 200, 'c': 300}

    if 200 in sample_dict.values():
        print('200 present in a dict')


# exer_7()


def exer_8():
    # Rename key of a dictionary
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }

    sample_dict['location'] = sample_dict.pop("city")  # rename key
    print(sample_dict)


# exer_8()

def exer_9():
    # Get the key of a minimum value from the following dictionary
    sample_dict = {
        'Physics': 82,
        'Math': 65,
        'history': 75
    }

    # geting maximum key
    print(max(sample_dict))
    print(max(sample_dict.values()))
    print(max(sample_dict.items()))

    # geting minimum key, value and  item
    print(min(sample_dict))
    print(min(sample_dict.values()))
    print(min(sample_dict.items()))


# exer_9()


def exer_10():
    # Change value of a key in a nested dictionary
    sample_dict = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 500}
    }

    sample_dict['emp3']['salary'] = 8500
    print(sample_dict)

    for i in sample_dict.values():
        print(i['name'])



# exer_10()



def exer_11():
    # multiple dictionaries inside a single dictionary
    jessa = {'name': 'Jessa', 'state': 'Texas', 'city': 'Houston', 'marks': 75}
    emma = {'name': 'Emma', 'state': 'Texas', 'city': 'Dallas', 'marks': 60}
    kelly = {'name': 'Kelly', 'state': 'Texas', 'city': 'Austin', 'marks': 85}
    # jessa.clear()
    print(jessa)
    class_six = {"student1": jessa, "student2": emma, "student3": kelly}

    print(class_six)

    for key, value in class_six.items():
        print(key)
        # display each student data
        for nested_key, nested_value in value.items():
            print(f"{nested_key} : {nested_value}")

# exer_11()
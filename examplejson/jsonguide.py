import json

# bad codes but need for realizing
# json_changer_file = open('examplejson/example.json', 'w')
# json_reader_file = open('examplejson/example.json', 'r')


def exer_1():
    # json dump methodi  python dictdan jsonga concert qilib beradi
    data = {"key1": "value1", "key2": "value2"}
    result = json.dumps(data, indent=1)
    # print(result)
# exer_1()


def exer_2():
    # example = json.load(json_file)
    # print(example)
    # with open('examplejson/example.json','r' ) as example_json:
    #     result = json.load(e)
    #     print(result)
    a = 10


# exer_2()


def task1():
    global json_changer_file
    person = {"name": "Aziza", "age": 21, "city": "Tashkent"}
    result = json.dumps(person, indent=4)
    print(result)
    json_changer_file.write(result)


# task1()


def task2():
    data = '{"product": "phone", "price": 350, "in_stock": true}'
    result = json.loads(data)
    print(result)


# task2()


def task3():
    info = {"id": 123, "status": "active", "balance": 1000}
    with open("examplejson/info.json", 'w') as info_file:
        # dump file object kutadi => open() chunki unda write methodi bor
        result = json.dump(info, fp=info_file)


# task3()


def task4():
    with open('examplejson/info.json', 'r') as info:
        data = json.load(info)
        print(data.get('balance'))


# task4()


def task5():
    student = {
        "name": "Bekzod",
        "grades": [90, 85, 100],
        "passed": True
    }

    result = json.dumps(student)
    print(result)


# task5()


def task6():
    data = {"nums": (1, 2, 3)}
    result = json.dumps(data)
    # json tuple, set, complex, date time tipdegi malumotlarni qabul qilmaydi
    print(result)
    # tuple ozgaradi listga jsonda


# task6()


def task7():
    library = {
        "title": "Python Guide",
        "pages": 250,
        "authors": ["Ali", "Lola"]
    }
    result = json.dumps(library, indent=4)
    print(result)


# task7()

def task8():
    bad_json = '{"name": "Rustam", "age": 28}'

    try:
        result = json.loads(bad_json)
        print(result)
    except json.JSONDecodeError as e:  # agar jsonda qandaydur hato bolsa ushlab olib console qilish
        print(f'Json decode error: {e}')


# task8()


def greater_than_80_grade():
    with open("examplejson/info.json", 'r') as json_file:
        data = json.load(json_file)
        print(data)
        for i in data:
            if i['grade'] >= 80:
                print(i)


# greater_than_80_grade()


def formater_json():
    employee = {
        "id": 101,
        "info": {
            "name": "Malika",
            "department": "HR",
            "skills": ["communication", "recruitment", "negotiation"]
        }
    }
    result = json.dumps(employee, indent=4)
    print(result)

# formater_json()


def cuting_json():
    with open('examplejson/expl.json', 'r') as json_file:
        data = json.load(json_file)
        # first solution
        for items in data:
            # name qiriqib tashash ve yengi
            # dict comprehension
            result = {k: items[k] for k in items.keys() - {'name'}}
            print(result)

        # second solution
        for i in data:
            i.pop('name')
            print(i)


# cuting_json()

def catch_json_error():
    bad_data = '''
        {
        "title": "Book",
        "author": "Ali",
        "price": 250,
        }
    '''
    try:
        result = json.loads(bad_data)
    except json.JSONDecodeError as e:
        print(f'there have error: {e}')


# catch_json_error()


def geting_users_by_active_status():
    try:
        with open("examplejson/users.json", 'r') as json_file:
            data = json.load(json_file)
            cnter = 0
            for i in data.get('users', []):
                if i["active"] == True:
                    cnter += 1
            print(f"Faol foydalanuvchilar soni: {cnter}")
    except FileNotFoundError:
        print('fayl not found')
    except json.JSONDecodeError as e:
        print(f"json error: {e}")


geting_users_by_active_status()

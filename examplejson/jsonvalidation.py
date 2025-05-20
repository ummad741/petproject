import json
from typing import Optional, Union
from jsonschema import validate, ValidationError


try:
    with open('examplejson/users.json', 'r') as json_file:
        global_data = json.load(json_file)
except FileNotFoundError:
    print("Fayl Not Found ")
except json.JSONDecodeError as e:
    print(f"json error {e}")


def read_json_team_info(data):
    # there have bad codes
    #     print(data.get("json_task", None).get('team').get("members"))
    #     print(data.get("json_task", None).get('team').get("projects"))

    # clear code
    team = data.get('task1', {}).get('team', {})
    print(team.get('members', 'no members found'))
    print(team.get('projects', 'no project found'))
    # task2
    length_of_object = len(team.get('members', []))
    print(length_of_object)

# read_json_team_info(global data)


def word_checker(data, word='python'):

    check_list = data.get('task5', {}).get('employee', {}).get('skills', [])
    # print(check_list)
    # first solution
    result = True if word in check_list else False
    # second solution
    result = word in check_list
    print(result)


word_checker(global_data)  # dependency injection(DI)


# JsonValidationSChema
try:
    with open("examplejson/schema.json", "r") as json_file:
        global_data_for_schema = json.load(json_file)
except FileNotFoundError:
    print("File Not Found")
except json.JSONDecoder as e:
    print(f"Json Error")


def adding_required_arguments(data: dict):
    schema = {
        "type": "object",
        "properties": {
            "name": {'type': 'string'},
            "age": {'type': 'integer'},
            "email": {
                "type": "string",
                "format": "email"

            }
        },
        'required': ['name', 'age']
    }
    try:
        validate(instance=data.get("task1", {}), schema=schema)
        print("json is valid 1")
    except ValidationError as e:
        print(f"Validation Error: {e.message}")


adding_required_arguments(global_data_for_schema)


def working_with_array(data: dict):
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "tags": {
                "type": "array",
                "minItems": 1,
                "maxItems": 3
            },
            "test": {"type": "string"}
        },
        "required": ["id", "tags"]
    }

    try:
        validate(instance=data.get("task2", {}), schema=schema)
        print("Json Is Valid 2")
    except ValidationError as e:
        print(e.message)


working_with_array(global_data_for_schema)


def working_with_object(data: dict):
    schema = {
        "type": "object",
        "properties": {
            "product": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "minLength": 5,
                        "maxLength": 20
                    },
                    "price": {
                        "type": "integer",
                        "minimum": 100,
                        "maximum": 3000
                    },

                },
                "required": ["title", "price"]
            }
        },
        "required": ["product"]
    }
    try:
        validate(instance=data.get("task3", {}), schema=schema)
        print("Json Is Valid 3")
    except ValidationError as e:
        print(e.message)


working_with_object(global_data_for_schema)


def task4(data: dict):
    schema = {
        "type": "object",
        "properties": {
            "user": {
                "type": "object",
                "properties": {
                    "username": {"type": "string"},
                    "verified": {"type": "boolean"},
                    "roles": {
                        "type": "array",
                        "minItems": 1
                    }
                },
                "required": ["username", "verified"]
            }

        },
        "required": ["user"]
    }

    try:
        validate(instance=data.get("task4", {}), schema=schema)
        print("Json Is Valid 4")
    except ValidationError as e:
        print(e.message)


task4(global_data_for_schema)


def task5(data: dict):
    schema = {
        "type": "object",
        "properties": {
            "users": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "active": {"type": "boolean"}
                    },
                    "required": ["id", "active"]
                }
            },
            "test": {
                "type": "array",
                "items": {"type": "string"}
            }
        },
        "required": ["users"]
    }

    try:
        validate(instance=data.get("task5", {}), schema=schema)
        print("Json Is Valid 5")
    except ValidationError as e:
        print(e.message)


task5(global_data_for_schema)


def schema_maker():
    # task6
    schema_methods = {
        "type": "object",
        "properties": {
            "user": {
                "type": "object",
                "properties": {
                    "username": {
                        "type": "string",
                        "minLength": 5
                    },
                    "email": {
                        "type": "string",
                        "format": "email"
                    },
                    "phone": {
                        "type": "string",
                        "pattern": "^\d+$"
                    },
                },
                "required": []

            }
        },
        "required": []
    }
    # task 7
    schema2 = {
        "type": "object",
        "properties": {
            "categories": {
                "type": "array",
                "minItems": 2,
                "uniqueItems": True
            }
        },
        "required": []
    }
    # task8
    schema_enum = {
        "type": "object",
        "properties": {
            "status": {
                "type": "string",
                "enum": ["pending", "aproved", "rejected"]

            }  # status berilgan 3 qiymat oladi
        },
        "required": []
    }
    # task9
    schema_nested = {
        "type": "object",
        "properties": {
            "products": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "name": {"type": "string"},
                        "price": {
                            "type": "integer",
                            "minimum": 0
                        },
                    },


                }

            }
        },
        "required": []
    }
    # task10
    schema_conditional_logic = {
        "type": "object",
        "properties": {
            "type": {"type": "string"},
            "details": {"type": "object"}
        },
        "required": ["type", "details"],

        "if": {
            "properties": {
                "type": {"const": "student"}
            }
        },
        "then": {
            "properties": {
                "details": {
                    "type": "object",
                    "properties": {
                        "grade": {"type": "integer"}
                    },
                    "required": ["grade"]
                }
            }
        },
        "else": {
            "properties": {
                "details": {
                    "type": "object",
                    "properties": {
                        "experience": {"type": "integer"}
                    },
                    "required": ["experience"]
                }
            }
        }
    }

    # patternproperties regex bilan ishlidi
    schema_patternproperties = {
        "type": "object",
        "patternProperties": {
            # Patternproperties keyvordga regex bn validate qoshish
            "^item_": {"type": "integer"}  # regex
        },
        # boshqa qiymatlarni rad etadi korsatilgan qiymatlarni qabul qiladi
        # propertiydegi shablon korinishida ishidi
        "additionalProperties": False,
    }
    # additionalProperties schemadan tashqaridegi malumotlar kelsa ular string typeida bolishi kerak boladi
    schema_additionalproperties = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"}
        },
        "required": ["name", "age"],
        "additionalProperties": {
            "type": "string"
        }

    }

    # one of u yoki bu qiymat bolishi kerak lekin ikkalsi birga bololmaydi
    schema_oneof = {
        "type": "object",
        "properties": {
            "value": {}
        },
        "required": ["value"],
        "oneof": [
            {
                "properties": {
                    "value": {"type": "string"}
                }
            },
            {
                "properties": {
                    "value": {"type": "integer"}
                }
            }
        ]
        # test:
        # value int yoki str bolishi kerak boshqa qiymatlar olmidi yoki u yoki bu
        # va ikkita qiymat baravariga bolishi mumkun emas
    }

    # any of da berilgan validatelarni bittasi tori kelsaham jsonga valida beradi yani shablonga mos ruxsat bor
    schema_anyof = {
        "type": "object",
        "properties": {
            "value": {}
        },
        "required": ["value"],
        "anyOf": [
            {
                'properties': {
                    "value": {
                        "type": "string",
                        "minLength": 3
                    }
                }
            },
            {
                'properties': {
                    "value": {
                        "type": "integer",
                        "minimum": 10
                    }
                }
            }
        ]

        # hop data integer yoki string va ularga berilgan validatega tori kelsa json valid boladi,
        # birdaniga ikkita qiymat kelsa error beradi
    }

    # allOf ichidagi barcha schema shartlari bajarilishi shart.
    schema_allof = {
        "type": "object",
        "properties": {
            "value": {}
        },
        "required": ["value"],
        "allOf": [
            {
                "properties": {
                    "value": {"type": "string"}
                }
            },
            {
                "properties": {
                    "value": {"minLength": 3}
                }
            }
        ]
    }

    # dependencies — bu biror bir maydon (field) mavjud bo‘lsa, yana boshqa maydon(lar) ham bo‘lishi kerak degan qoida.
    schema_dependency = {
        "type": "object",
        "properties": {
            "username": {"type": "string"},
            "password": {"type": "string"},
            "confirm_password": {"type": "string"}
        },
        "required": ["username"],
        "dependencies": {
            "password": ["confirm_password"]
        }
    }
    # bu nma digani agar password bolsa confir password ham bolishi shart
    # agar password bolmasa confirmni keragi ham bolmaydi
    # real analog: yomgir yogsa bulut bolishi shart yomgir yogmasa bulut bolmaydi


schema_maker()


try:
    with open('examplejson/irontrack.json', 'r') as irontrack_file:
        data_irontrack = json.load(irontrack_file)
except FileNotFoundError:
    print("file not found")
except json.JSONDecodeError as e:
    print(f'json error: {e}')


def irontrack_1(data: dict):
    schema = {
        "type": "object",
        "patternProperties": {
            '^user_': {"type": "string"}
        },
        "required": [],
        "additionalProperties": False
    }
    try:
        # valid json test
        validate(
            instance=data.get('task1', {}).get("valid_json", {}),
            schema=schema
        )
        print("irontrack valid json_1")
    except ValidationError as e:
        print(f"validation error: {e.message}")


def irontrack_2(data: Optional[dict]):
    schema = {
        "type": "object",
        "patternProperties": {
            '^attr_': {"type": "boolean"}
        },
        "required": [],
        "additionalProperties": False
    }

    try:
        validate(
            instance=data.get('task2', {}).get('valid_json'),
            schema=schema
        )
        print("irontrack valid json_2")

    except ValidationError as e:
        print(f"json error {e.message}")


def irontrack_3(data: Optional[dict]):
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"}
        },
        "required": ["name", "age"],
        "additionalProperties": {
            "type": "string"
        }
    }

    try:
        validate(
            instance=data.get('task3').get('valid_json'),
            schema=schema
        )
        print("irontrack valid json_3")

    except ValidationError as e:
        print(f"json error {e.message}")


def irontrack_4(data: dict):
    # const vs enum
    # const bitta qatiy qiymat
    # enum choise bir nechta qiymat
    schema = {
        "type": "object",
        "properties": {
            "payment_method": {"type": "string"},
        },
        "required": ["payment_method"],
        "oneOf": [
            {
                "properties": {
                    "payment_method": {"const": "card"}
                }
            },
            {
                "properties": {
                    "payment_method": {"const": "paypal"}
                }
            }
        ]
    }
    try:
        validate(
            instance=data.get('task4').get('valid_json'),
            schema=schema
        )
        print("irontrack valid json_4")
    except ValidationError as e:
        print(f"json error {e.message}")


def irontrack_5(data: dict):
    # contact string yoki null qiyma oladi hudi
    # enumga oxshaydi faqat u keyvord qanday qiymat olishini korsatadi
    schema = {
        "type": "object",
        "properties": {
            "contact": {}
        },
        "required": ["contact"],
        "anyOf": [
            {
                "properties": {
                    "contact": {"type": "string"}
                }
            },
            {
                "properties": {
                    "contact": {"type": "null"}
                }
            }
        ]
    }
    try:
        validate(
            instance=data.get("task5", {}).get("valid_json"),
            schema=schema
        )
        print("irontrack valid json_5")

    except ValidationError as e:
        print(f"validation error: {e}")


def irontrack_6(data: dict):
    schema = {
        "type": "object",
        "properties": {
            "age": {}
        },
        "required": ["age"],
        "anyOf": [
            {
                "properties": {
                    "age": {
                        "type": "integer",
                        "minimum": 18,
                        "maximum": 65
                    }
                }
            },
        ]
    }
    print(data.get("task6", {}).get("valid_json"))
    try:
        validate(
            instance=data.get("task6", {}).get("valid_json"),
            schema=schema
        )
        print("irontrack valid json_6")

    except ValidationError as e:
        print(f"validation error: {e}")


def irontrack_7(data: dict):
    schema = {
        "type": "object",
        "properties": {
            "vehicle": {"type": "string"},
            "license_plate": {"type": "string"},
        },
        "required": ["username"],
        "dependencies": {
            "vehicle": ["license_plate"]
        }
    }
    try:
        validate(
            instance=data.get("task7", {}).get("valid_json"),
            schema=schema
        )
        print("irontrack valid json_7")

    except ValidationError as e:
        print(f"validation error: {e}")


def irontrack_8(data: dict):
    schema = {
        "type": "object",
        "properties": {
            "credit_card": {"type": "integer"},
            "billing_address": {"type": "string"},
            "cvv": {"type": "integer"}
        },
        "required": ["credit_card"],
        "dependencies": {
            "credit_card": ["billing_address", "cvv"]
        }
    }
    try:
        validate(
            instance=data.get("task8", {}).get("valid_json"),
            schema=schema
        )
        print("irontrack valid json_8")

    except ValidationError as e:
        print(f"validation error: {e}")


def irontrack_9(data: dict):
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "status": {
                "type": "string",
                # short way
                "enum": ["active", "inactive", "pending"]
            },
        },
        "required": ["status"],
        # oneOf variant
        "oneOf": [
            {
                "properties": {
                    "status": {"const": "active"}
                }
            },
            {
                "properties": {
                    "status": {"const": "inactive"}
                }
            },
            {
                "properties": {
                    "status": {"const": "pending"}
                }
            }
        ]
    }

    try:
        validate(
            instance=data.get("task9", {}).get("valid_json"),
            schema=schema
        )
        print("irontrack valid json_9")

    except ValidationError as e:
        print(f"validation error: {e}")


irontrack_1(data_irontrack)
irontrack_2(data_irontrack)
irontrack_3(data_irontrack)
irontrack_4(data_irontrack)
irontrack_5(data_irontrack)
irontrack_6(data_irontrack)
irontrack_7(data_irontrack)
irontrack_8(data_irontrack)
irontrack_9(data_irontrack)


# working on $ref method DRY

def working_on_ref():
    schema = {
        "#schema":"http://json-schema.org/draft-07/schema#",
        "definitions": {
            "person": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "age": {"type": "integer"}
                },
                "required": ["name", "age"]
            }
        },
        "type": "object",
        "properties": {
            "student": {"$ref": "#/definitions/person"},
            "teacher": {"$ref": "#/definitions/person"}
        },
        "required": ["student", "teacher"]
    }

    with open("examplejson/test.json", 'r') as file:
        data = json.load(file)
        print(data)
    try:
        validate(instance=data, schema=schema)
        print("✅ Validation passed")
    except ValidationError as e:
        print(f"❌ validation error: {e}")


# working_on_ref()

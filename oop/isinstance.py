
# what is isinstance()

# isinstance() cheking type of variable
# isinstance() ozgaruvchilarini type tekshiradi ayniqsa functionlarda foydasi kotta


# examples

a = 10
print(isinstance(a, int))  # true

print(isinstance(a, str))  # False


# multiple checking kop typelar bilan tekshirish ozgaruvchini

b = 'checking', 10  # it's type tuple

print(isinstance(b, (int, str, tuple)))  # True


# checking function

def sample(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a+b

    return 'type error must be int '


# print(sample(1, 2))


a = "abcd"
b = "xyzo"
print(a[:2] + b[2:]+ ' ' + b[:2]+a[2:])


def func(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return list((new_a, new_b))

print(func(a,b))

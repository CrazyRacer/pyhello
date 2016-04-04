from functools import reduce


def f(x):
    return x ** 2


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def add(x, y):
    return x * 10 + y


print(reduce(add, [1, 3, 5, 7, 9]))


def normalize(name):
    return name.title()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    def mul(x, y):
        return x * y

    return reduce(mul, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


# def str2float(s):
#     def
#
# print('str2float(\'123.456\') =', str2float('123.456'))

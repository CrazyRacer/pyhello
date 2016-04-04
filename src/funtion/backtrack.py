def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(120))


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)


print(move(10, 'A', 'B', 'C'))

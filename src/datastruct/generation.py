g = (x * x for x in range(10))


# print(next(g))


def fib(right):
    n, a, b = 0, 0, 1
    while n < right:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


f = fib(6)

for i in f:
    print(i)


# N=[1,0]
# print(N[-1]+N[0])


def triangles():
    N = [1]
    while True:
        yield N
        N.append(0)
        N = [N[i - 1] + N[i] for i in range(len(N))]


n = 0
for t in triangles():
    n += 1
    print(t)
    if n == 100:
        break

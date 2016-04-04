import math


def quadratic(a, b, c):
    result = {}
    if a == 0:
        # 一元一次方程
        if b == 0:
            if c == 0:
                print('恒等式')
                result = None
            else:
                print('方程无解')
                result = None

        else:
            x = -c / b
            result[0] = x
    else:
        z = b ** 2 - 4 * a * c
        if z < 0:
            print('方程无实数根')
            result = None
        else:
            sqrt = math.sqrt(z)
            x = (-b + sqrt) / (2 * a)
            y = (-b - sqrt) / (2 * a)
            result[0] = x
            result[1] = y
    return result

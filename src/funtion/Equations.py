import math


def quadratic(a, b, c):
    sqrt = math.sqrt(b ** 2 - 4 * a * c)
    x = (-b + sqrt) / (2 * a)
    y = (-b - sqrt) / (2 * a)
    return x, y

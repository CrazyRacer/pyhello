import math
from src.funtion.abstest import my_abs

print(my_abs(-1))


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
r = move(100, 100, 60, math.pi / 6)
# 函数返回多个值其实就是返回一个tuple元祖
print(r)

from src.funtion.equations import quadratic

print(quadratic(2, 3, 1))
print(quadratic(0, 0, 0))
print(quadratic(0, 0, 1))
print(quadratic(2, -1, 1))
print(quadratic(0, -1, 1))

result = quadratic(0, -1, 1)
print('方程的解为', result)

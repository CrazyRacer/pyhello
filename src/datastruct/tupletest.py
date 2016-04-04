# tuple 一但初始化不能修改
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

# 请注意以下声明方式不是元祖而是数字
t = (1)
print(t)

# 正确的声明元祖的方式
t = (1,)
print(t)

# 元祖中的list是可以修改的
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
print(t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])
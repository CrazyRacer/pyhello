age = 20
if age >= 18:
    print('your age is', age)
    print('audit')
else:
    print('your age is', age)
    print('teenager')

# input 返回类型为str 需要类型转换
# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

height = 1.75
weight = 80.5

bmi = weight / (height ** 2)
print(bmi)

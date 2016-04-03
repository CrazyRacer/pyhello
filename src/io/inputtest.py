# coding=utf-8
# name = input('please enter your name: ')
# print('hello,', name)

# 使用\来对'进行转义
print('I\'m ok.')
print('I\'m learning\nPython.')
# r 标识去除转义
print(r'\\\t\\')

print(r"I'm ok")
print('''line1
... line2
... line3''')

print('''line1
line2
line3''')

print(True and False)

print(5 > 3)
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n)
print(f)
print(s2)

s1 = 10
s2 = 4
print(s1//s2)
print(s1%s2)
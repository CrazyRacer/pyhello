print('包含中文的str')
print(ord('A'))
print(ord('中'))
print(chr(66))
print('\u4e2d\u6587')
x = b'ABC'
print(x)
print(len('中文'.encode('utf-8')))
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

print('%030d-%02d' % (30, 1))
print('%.2f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d %%' % 7)

# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：

print('%.1f%%' % ((85 - 72) / 72 * 100))
s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

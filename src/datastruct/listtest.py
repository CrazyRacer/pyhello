# list是一种有序的集合
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

# len函数获取list的长度
print(len(classmates))

print(classmates[0])

# 索引越界会报IndexError错误


# 使用-1直接获取倒数第一个元素 -2倒数第二个元素
print(classmates[-1])

# 向list中增加元素
classmates.append('Adam')
print(classmates)

# list末尾去掉一个元素(pop默认为-1即末尾元素)
classmates.pop()
print(classmates)

# 向list指定位置插入元素
classmates.insert(1, 'Jack')
print(classmates)

# list去掉索引1的元素
classmates.pop(1)
print(classmates)

# 元素替换
classmates[1] = 'Sarah'
print(classmates)

# list元素数据类型可以不同
L = ['Apple', 123, True]

# 可以list套list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))

print(s[2][0])

L = []
print(len(L))

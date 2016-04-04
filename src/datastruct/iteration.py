from collections import Iterable

# 判断对象是否支持迭代
print(isinstance('abc', Iterable))
print(isinstance(1, Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(True, Iterable))

# python enumerate函数可将list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# 查找
print(d['Michael'])
# 赋值
d['Adam'] = 67
print(d)
d['Adam'] = 68
print(d)
# 判断key是否存在的几个办法
print('Adam' in d)
# 返回None
print(d.get('o'))

# 返回-1
print(d.get('0', -1))

# 删除key
d.pop('Bob')
print(d)

# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

# list不可作为dict的key 因为list可变
# key = [1, 2, 3]
# d[key] = 'a list'



m ={}
m[0]=1
print(m)
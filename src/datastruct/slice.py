# 取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：

l = ['michael', 'sarah', 'bob', 'jack']

# 表示从0开始 , 3结束 , 不包括3
print(l[0:3])
# 表示从0开始 , 2结束 , 不包括2
print(l[:2])
# 倒数切片
print(l[-4:-1])
# 前10个美俩个取一个
print(l[:10:2])
print(l[::5])


print(l[::2])

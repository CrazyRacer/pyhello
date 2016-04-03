s = set([1, 2, 3])
print(s)

s.add(4)
print(s)
s.add(4)

s.remove(4)

print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# set也是不能装list key的
# key = [1, 2, 3]
# s = set([key, 1, 3])

tt = (1, 2, 3)

s1 = set([tt, 2])
print(s1)

# 有可变对象就不能当key
t2 = (1, [2, 3])
s2 = set([t2, 1])

# 函数的参数

# 带有默认参数n的函数
def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


# 上述函数包含两个参数一个必选参数一个默认参数
# 当函数有多个参数时, 把变化大的参数放在前面 , 变化小的参数放后面 , 变化小的参数可以作为默认参数
print(power(2, 3))


# 特别注意

def add_end(l=[]):
    l.append('END')
    return l


add_end()
# 两次调用 add_end发现结果不对 , 是因为传入的数据结构为可变的 , 所以默认参数必选指向不变对象
print(add_end())


# 设置l为不可变参数None即可
def add_end(l=None):
    if l is None:
        l = []
    l.append('END')
    return l


add_end()
print(add_end())


# 传入可变参数*
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n ** 2
    return sum


print(calc(1, 2, 2))
# 通过*给list解包
nums = [1, 2, 3]
print(calc(*nums))


# 关键字参数 **自动包装成一个字典  **为字典的加包与解包 kw得到的是函数的拷贝 不会影响源
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('a', 2, bj='1')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

# 这叫命名关键字 如果要限制关键字函数 传入的key 使用*,
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')

# 参数定义顺序 参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。


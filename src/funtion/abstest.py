def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
        # print(abs(-20))
        # # 将a指向函数abs
        # a = abs
        # print(a(-1))

import re


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def cal(flag, a, b):
    if re.match('add', flag):
        return add(a, b)
    elif re.match('sub', flag):
        return sub(a, b)
    elif re.match('mul', flag):
        return mul(a, b)
    elif re.match('div', flag):
        return div(a, b)
    else:
        return 'err'


operation = input('请输入操作码（add, sub, mul, div）:')
n, m = input('请输入两个数').split(' ')
print('计算结果为：', cal(operation, int(n), int(m)))

import math


def showPower(n):
    return math.pow(2, n)


num = int(input('请输入想查看2的几次方：'))
print('结果为', showPower(num))

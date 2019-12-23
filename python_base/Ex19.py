import math


def isArmstrong(num):
    sum = int(0)
    n = int(num)
    while n != 0:
        temp = int(n % 10)
        n = int(n / 10)
        sum += math.pow(temp, 3)
    if sum == num:
        return True
    else:
        return False


num = int(input('请输入一个三位数整数：'))

if isArmstrong(num):
    print(num, '是水仙花数')
else:
    print(num, '不是水仙花数')

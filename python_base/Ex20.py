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


num = int(input('请输入范围最大值：'))

for i in range(100, num):
    if isArmstrong(i):
        print(i, end=' ')

def getFactor(num):
    arr = []
    for i in range(1, num):
        if num % i == 0:
            arr.append(i)
    return arr


num = int(input('请输入一个数：'))

print('因子为', getFactor(num))
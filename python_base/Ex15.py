def isPrimeNum(num):
    if num == 1 or num == 2:
        return True
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True


maxNum = int(input('请输入一个最大数：'))

for n in range(1, maxNum):
    if isPrimeNum(n):
        print(n, end=' ')

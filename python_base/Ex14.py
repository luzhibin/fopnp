def isPrimeNum(num):
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True


num = int(input('请输入一个整数：'))

if isPrimeNum(num):
    print('质数')
else:
    print('合数')

def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n - 1)


i = int(input('输入一个整数：'))
print(i, '的阶乘为', Factorial(i))

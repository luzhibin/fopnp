def Fibonacci(n):
    if n <= 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


n = int(input("输入一个正整数n，n为输出项数:"))
for i in range(1, n + 1):
    print(Fibonacci(i), end=' ')

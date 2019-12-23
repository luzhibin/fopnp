def max(a, b):
    return a if (a > b) else b


num1 = float(input('输入第一个数：'))
num2 = float(input('输入第二个数：'))
num3 = float(input('输入第三个数：'))

res = max(num1, max(num2, num3))

print('最大的数是：', res)

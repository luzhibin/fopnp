def sum(n):
    if n == 1:
        return 1
    else:
        return sum(n - 1) + n


i = int(input('输入一个整数：'))
print('其整数之和为：', (sum(i)))

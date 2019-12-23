def isPlus(num):
    if num > 0:
        return True
    else:
        return False


n = float(input('请输入一个数：'))

print('这是一个正数' if (isPlus(n)) else '这是一个负数')

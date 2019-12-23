def swop(a, b):
    return b, a


x = input("输入x的值：")
y = input("输入y的值：")

x, y = swop(x, y)

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

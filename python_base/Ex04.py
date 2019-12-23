def getTriangleArea(a, b, c):
    return (a + b + c) / 2


a = float(input('请输入第一条边：'))
b = float(input('请输入第二条边：'))
c = float(input('请输入第三条边：'))

print('面积为：', getTriangleArea(a, b, c))

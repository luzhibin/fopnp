import cmath


def getRes(a, b, c):
    d = (b ** 2) - (4 * a * c)
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    return sol1, sol2


a = float(input('输入二次项系数：'))
b = float(input('输入一次项系数：'))
c = float(input('输入常数项系数：'))

print('该方程结果为：', getRes(a, b, c))

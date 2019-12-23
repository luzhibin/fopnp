def add(a, b):
    return a + b


m, n = input('请输入两个数，用空格隔开：').split(' ')

print('{0} + {1} = {2}'.format(float(m), float(n), add(float(m), float(n))))

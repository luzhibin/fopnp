str = input('请输入一个字符串')

strList = list(str)
a = 0
e = 0
i = 0
o = 0
u = 0

for n in range(0, len(strList)):
    if strList[n] == 'a':
        a = a + 1
    elif strList[n] == 'e':
        e = e + 1
    elif strList[n] == 'i':
        i = i + 1
    elif strList[n] == 'o':
        o = o + 1
    elif strList[n] == 'u':
        u = u + 1

print('a:', a, 'e:', e, 'i:', i, 'o:', o, 'u:', u)

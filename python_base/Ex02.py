def sort(a, b):
    return (a, b) if (a > b) else (b, a)


n1, n2, n3 = input('请输入三个数，以空格隔开：').split(' ')
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

(n1, n2) = sort(n1, n2)
(n1, n3) = sort(n1, n3)
(n2, n3) = sort(n2, n3)

print("{}>{}>{}".format(n1, n2, n3))

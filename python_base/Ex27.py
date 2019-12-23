def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


n, m = input('请输入两个数').split(' ')

print(lcm(int(n), int(m)))

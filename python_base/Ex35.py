def dec2bin(n):
    result = "0"
    if n == 0:
        return result
    else:
        result = dec2bin(n // 2)
        return result + str(n % 2)


n = int(input("请输入一个十进制的数字："))
print(dec2bin(n))

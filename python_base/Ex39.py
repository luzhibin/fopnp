s = input("输入一个字符串:")
d = ''.join(reversed(s))
print(d)
if s == d:
    print("字符串是回文")
else:
    print("字符串不是回文")

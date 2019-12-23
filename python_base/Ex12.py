def isLeapYear(year):
    if year % 100 == 0:
        return True if (year % 400 == 0) else False
    else:
        return True if (year % 4 == 0) else False


year = int(input('请输入一个年份：'))

if isLeapYear(year):
    print('闰年')
else:
    print('不是闰年')

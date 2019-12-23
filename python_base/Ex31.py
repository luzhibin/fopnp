import calendar
# 设置第一天是星期天
calendar.setfirstweekday(firstweekday=6)

n = int(input('请输入所查看日历的级别 1（输出全年），2（输出某月）：'))

if n == 1:
    yy = int(input("输入年份: "))
    cal = calendar.TextCalendar()
    cal.pryear(yy)

if n == 2:
    yy = int(input("输入年份: "))
    mm = int(input("输入月份: "))
    print(calendar.month(yy, mm))

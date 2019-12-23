def km2mi(num):
    conv_fac = 0.621371
    return num * conv_fac


kilometers = float(input('请输入一个公里数：'))
print('%0.3f kilometers is equal to %0.3f miles' % (kilometers, km2mi(kilometers)))

def tdc2ftt(celsius):
    return (celsius * 1.8) + 32


celsius = float(input('请输入一个摄氏度值：'))
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' % (celsius, tdc2ftt(celsius)))

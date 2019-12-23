def getFibonacci(num):
    if num == 1:
        return [1]
    arr = [1, 1]
    for i in range(2, num):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr


num = int(input('请输入打印到Fibonacci第几项：'))
print('结果为', getFibonacci(num))

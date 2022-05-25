"""
100以内所有的质数


分析：只能被1和他本身整除
分解：
    1.如何判断一个数是质数
        1.1 意味着要从1开始测试，一直整除到他本身
        num = 7
        n = 2
        while n < 5:
            if num % n == 0
                break
            n += 1
        else:
            print()
    2.判断100以内的所有数


"""

num = int(input("please"))
n = 2
while n < num:
    if num % n == 0:
        print('num不是质数')
        break
    n += 1
else:
    print('num是质数')

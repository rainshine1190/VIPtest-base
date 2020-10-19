"""
求斐波那契数列 1 1 2 3 5 8 13 ……

分析：
    a b c d e f
    1 1 2 3 5
        n -2  n-1  n
第一种方法：
    list1 = [1,1]
    c = list1[0] + list[1]
    list1 = [1,1,2]
    d = list1[-1] + list[-2]

第二种方法
    a b c d e f
    1 1 2 3 5

    c = a + b
    b = b
    b = c


"""

list1 = [1,1]
m = 1
n = int(input("please input your num "))
while m <= n:
    num  = list1[-1] + list1[-2]
    list1.append(num)
    m += 1

print(list1)
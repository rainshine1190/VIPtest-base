#coding:utf-8
# __author__ = 'lc'


#定义函数calc-无参无返回值
def calc(x,y=1):
    # print(x,y)
    c = x/y
    return c
    # print('结果为：',c)
    # print('结果为：%d' % c)

#调用
# print(calc())
#

a = int(input('请输入一个数'))
b = int(input('请输入第二个数'))

result = calc(a)

print(result)



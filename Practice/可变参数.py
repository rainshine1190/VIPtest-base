#coding:utf-8
# __author__ = 'lc'

#可变参数

def calc(*args):
    print(*args)
    #args默认保存为元组***********
    print(args,type(args))
    for i in args:
        print('传入的值分别为：',i)


#可变参数传参形式1-常用
m = [1,2,3]
n = (3,4,5)
#通过引用的方式传入必须带星号************
calc(*m)
calc(*n)

#可变参数传参形式2
calc(1,2,3)

calc()
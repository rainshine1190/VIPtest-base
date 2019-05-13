#coding:utf-8
# __author__ = 'lc'

def fun1():
    print('我是fun1函数')

def fun2():
    print('我是fun2函数')


# fun1()
# fun2()
# print('我是被调用的模块！')

print('name值为：',__name__)


#说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
if __name__ == '__main__':
    fun1()
    fun2()


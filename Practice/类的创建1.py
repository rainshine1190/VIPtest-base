#coding:utf-8

# __author__ = 'lc'


#类的定义
class Person:
    #类方法
    def eat(self,food):
        print('%s吃%s' % (self.name,food))
        print(self.sleep())

    def sleep(self):
        print('睡觉')


# 第一步：实例化--创建一个对象（变量名=类名（））
a = Person('xiaoming')

# 第二步：调用类中的方法（实例名.方法名()）
a.eat('rice')

b = Person()
b.eat('mantou')



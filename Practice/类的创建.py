#coding:utf-8

# __author__ = 'lc'


#类的定义
class Person:
    #类属性
    # name = '小明'

    #实例属性
    #初始化方法，类中必须存在的且在实例化过程中自动被调用的方法

    def __init__(self,name):
        self.name = name
        print('此方法被调用！')
    #
    # def __init__(self):
    #     print('此方法被调用！')

    #自定义方法，方法属性
    def eat(self,food):
        print('%s吃%s' % (self.name,food))
        print(self.sleep())

    def sleep(self):
        print('睡觉')


class Teacher(Person):

    def __init__(self,gh,name):
        self.gh = gh
        self.name = name

    def teach(self,course):
        print('工号为：%s的老师教%s课' % (self.gh,course))
        print('名字为：%s的老师教%s课' % (self.name,course))
        print(Person.sleep(self))




#第一步：实例化--创建一个对象（变量名=类名（））
# a = Person('xiaoming')

#第二步：调用类中的方法（实例名.方法名()）
# a.eat('rice')

# b = Person()
# b.eat('mantou')



a = Teacher(98,'xiaohong')

a.teach('math')


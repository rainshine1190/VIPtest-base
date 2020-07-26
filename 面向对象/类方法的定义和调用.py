#coding:utf-8
__author__ = 'lc'


class Person(object):

    #定义私有属性
    __money = 1000

    color = 'yellow'

    #构造方法，定义实例属性
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # print('执行init方法')

    def fun1(self,course):
        # print('self',id(self))
        print('执行fun1方法')
        print('对象的属性是：',self.name,self.age,course)

    @classmethod
    def fun2(cls):
        #两者等价，但是cls更通用，不然类名一发生变化则。。。
        return cls.color
        # return Person.color

    def __str__(self):
        '''返回一个对象的描述信息'''
        #类内部引用私有属性
        return "颜色是{},存款有{}".format(self.color,self.__money)

a1 = Person('大明',15)

#通过实例对象调用类方法
#调用实例方法：实例名.方法名

a1.fun1('math')
#调用类方法：1-实例名.方法名;2-类名.方法名
print(a1.fun2())
print(Person.fun2())


#总结:
#默认有个 cls 参数，可以被类和对象调用，
# 需要加上 @classmethod 装饰器。








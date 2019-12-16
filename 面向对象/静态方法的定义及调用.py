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

    @staticmethod
    def fun3():
        print('静态方法')

    def __str__(self):
        '''返回一个对象的描述信息'''
        #类内部引用私有属性
        return "颜色是{},存款有{}".format(self.color,self.__money)


#通过类对象调用类方法
print(Person.fun3())


#总结:
#用 @staticmethod 装饰的不带 self 参数的方法叫做静态方法，
#类的静态方法可以没有参数（cls,self），可以直接使用类名调用。







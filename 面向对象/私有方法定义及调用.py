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
        #类的内部调用私有方法
        self.__fun2()

    #定义私有方法
    def __fun2(self,course):
        # print('self',id(self))
        print('执行fun1方法')
        print('对象的属性是：',self.name,self.age,course)


    def __str__(self):
        '''返回一个对象的描述信息'''

        #类内部引用私有属性
        return "颜色是{},存款有{}".format(self.color,self.__money)


a1 = Person('大明',15)

# print(a1)

#类的外包引用私有方法
a1.__fun2()


#总结:
#1-私有方法必须__开头
#2-类的私有方法只能在类内部引用，不能再类外部引用






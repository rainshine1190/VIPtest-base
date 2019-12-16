#coding:utf-8
__author__ = 'lc'


class Person(object):

    #类属性，类中的集合公有的属性
    color = '黄色'

    #构造方法，定义实例属性
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # print('执行init方法')

    def fun1(self,course):
        # print('self',id(self))
        print('执行fun1方法')
        print('对象的属性是：',self.name,self.age,course)

    def __str__(self):
        '''返回一个对象的描述信息'''
        #引用类属性
        return "颜色是{}".format(self.color)

a1 = Person('大明',15)

print(a1)
#引用类属性-类对象访问
print('类对象访问',Person.color)
#引用类属性-实例对象访问
print('实例对象访问',a1.color)
#修改类属性
a1.color = 'red'
print(a1)




#总结：类属性不同于实例属性，类属性是类中的集合（类和实例）共同具有的属性，
# 而实例属性只属于实例本身，可以在类外部及内部使用







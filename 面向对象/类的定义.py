#coding:utf-8
__author__ = 'lc'

class Person(object):

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

a1 = Person('大明',15)
a1.fun1('math')
a1.sex = 'male'
print(a1.sex,a1.name)









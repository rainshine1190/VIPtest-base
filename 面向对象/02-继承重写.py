#coding:utf-8
# __author__ = 'lc'


class Animal:
    def eat(self):
        print('---------吃')
    def drink(self):
        print('---------喝')


class Dog(Animal):
    def bark(self):
        print('---------汪汪叫')


class Xiaotq(Dog):
    def fly(self):
        print('------飞')

    def bark(self):
        print('-------哮天犬狂叫')

    def can(self):
        self.fly()
        self.bark()
        super().bark()


x = Xiaotq()
# x.fly()
# x.bark()
#
# #重写：1-必须继承父类；2-重写的方法必须和父类的方法重名（一模一样）
#
# #子类可以拥有父类的父类的功能
# x.eat()
x.can()
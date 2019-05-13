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
        print('------狂叫')
        #第一种调用被重写的方法，父类的名字.方法名()
        Dog.bark(self)
        #第二种
        super().bark()

x = Xiaotq()
x.fly()
x.bark()
#子类可以拥有父类的父类的功能
x.eat()
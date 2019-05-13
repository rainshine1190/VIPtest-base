#coding:utf-8
# __author__ = 'lc'


class Animal:
    def eat(self):
        print('---------吃')
    def drink(self):
        print('---------喝')

class Dog:
    def eat(self):
        print('---------吃')
    def drink(self):
        print('---------喝')


class Dog(Animal):
    def bark(self):
        print('---------汪汪叫')


class Cat(Animal):
    def catch(self):
        print('-------抓老鼠')

#第一步：继承谁，类中的括号就写谁

#第二步：继承后，子类就具有父类的所有属性和方法，但是父类不能具备子类的属性和方法

#第三步：如果父类中没有子类需要的方法，可以在子类中自行定义

#注意：实例化和调用方法的时候要区分是否需要传参

wangcai = Dog()
wangcai.eat()
wangcai.bark()

# tom = Cat()
# tom.catch()



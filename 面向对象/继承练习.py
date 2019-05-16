#coding:utf-8
# __author__ = 'lc'


class Animal:

    def __init__(self,color):
        self.color = color

    def eat(self):
        print('---吃')
        print(self.color)

    def drink(self):
        print('---喝')


class Dog(Animal):

    def __init__(self,name,color):
        self.color = color
        self.name = name
        print(self.name,self.color)

    def bark(self):
        print('---汪汪叫')
        self.eat()


d = Dog('德牧','black')
d.bark()
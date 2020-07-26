#coding:utf-8
# __author__ = 'lc'

#
# class Animal():
#     def eat(self):
#         print('---------吃')
#     def drink(self):
#         print('---------喝')
#
# class Dog(Animal):
#     def bark(self):
#         print('--------汪汪汪')
#
#
# #继承：1-要继承谁（类），就在括号中写谁；2-继承谁就拥有了谁的属性和方法
# class Person(Animal):
#     pass
#
#
# #继承：子类可以调用父类的所有属性和方法，子类还可以调用自己的属性和方法(父类不能调用子类的属性和方法)
#
# d = Dog()
# d.eat()
# d.bark()
#
# a = Animal()
# a.eat()
# a.drink()
# a.bark()

#-------------------------------子类定义自身属性
#
# class Animal():
#     def __init__(self,name):
#         self.name = name
#
#     def eat(self):
#         print(f'{self.name}---------吃')
#     def drink(self):
#         print(f'{self.name}---------喝')
#
#
# #当子类书写了构造方法后，一定要在其中调用父类的构造方法来对父类的属性进行初始化
# #当你继承了别人，就要对别人的属性进行初始化
# class Dog(Animal):
#     def __init__(self,name,brand):
#         # super(Dog, self).__init__(name)
#         super().__init__(name)
#
#         self.brand = brand
#
#     def bark(self):
#         print('--------汪汪汪')
#
# d = Dog('小花','国美犬')
# print(d.name,d.brand)
















# class Dog(Animal):
#     def bark(self):
#         print('---------汪汪叫')
#
#
# class Cat(Animal):
#     def catch(self):
#         print('-------抓老鼠')
#
# #第一步：继承谁，类中的括号就写谁
#
# #第二步：继承后，子类就具有父类的所有属性和方法，但是父类不能具备子类的属性和方法
#
# #第三步：如果父类中没有子类需要的方法，可以在子类中自行定义
#
# #注意：实例化和调用方法的时候要区分是否需要传参
#
# wangcai = Dog()
# wangcai.eat()
# wangcai.bark()
#
# # tom = Cat()
# # tom.catch()



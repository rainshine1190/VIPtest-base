#coding:utf-8

# Python练习题：
# 1、打印小猫爱吃鱼，小猫要喝水
class Cat():

    def eat(self,food):
        print('小猫爱吃%s'%food)

    def drink(self,juice):
        print('小猫要喝%s'%juice)

c = Cat()
c.eat('fish')
c.drink('water')


#coding:utf-8

# Python练习题：
# 1、打印小猫爱吃鱼，小猫要喝水

#分析步骤
#1.需要定义类-cat猫
#2.类的属性和方法
#   2.1属性-无
#   2.2方法-吃鱼/喝水



class Cat(object):

    def eat(self,food):
        print('小猫爱吃%s'%food)

    def drink(self,juice):
        print('小猫要喝%s'%juice)

c = Cat()
c.eat('fish')
c.drink('water')


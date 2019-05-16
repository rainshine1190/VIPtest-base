#coding:utf-8
__author__ = 'lc'

"""
实例属性：   和具体的某个实例对象有关系，并且一个实例对象和另外一个实例对象是不同享实力属性的

类属性：类属性所属于类对象，并且多个实例对象之间共享一个类属性
"""


# class Tool:
#
#     num = 0
#
#     def __init__(self,name):
#         self.name = name
#         Tool.num += 1
#
#
# t1 = Tool('铁锹')
# t2 = Tool('工兵铲')
#
# print(Tool.num)




class People(object):
    country = 'china' #类属性


print(People.country)
p = People()
print(p.country)
p.country = 'japan'
print(p.country)      #实例属性会屏蔽掉同名的类属性
print(People.country)
del p.country    #删除实例属性
print(p.country)

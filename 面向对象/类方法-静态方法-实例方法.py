#coding:utf-8
__author__ = 'lc'


class Game(object):

    #类属性
    num = 0

    #实例方法
    def __init__(self):
        #实例属性
        self.name = 'laowang'

    #类方法
    @classmethod
    def add_num(cls):
        Game.num += 1

    #静态方法，允许参数为空，也可以有参数，不像实例方法和类方法，必须有self和cls作为参数代表实例或类的引用
    @staticmethod
    def print_menu():
        print('------------')
        print('  穿越火线1.1')
        print('  1-开始游戏')
        print('  2-结束游戏')
        print('------------')

g1 = Game()
#可以通过累的名字调用类的方法
Game.add_num()
#还可以通过这个类创建出来的对象去调用这个类方法
g1.add_num()

print(Game.num)

#通过类 去调用静态方法
Game.print_menu()
#通过实例对象 去掉用静态方法
g1.print_menu()









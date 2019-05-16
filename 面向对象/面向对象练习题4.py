#coding:utf-8

#  
# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量


class Gun():

    def __init__(self,name,bullet_count):
        self.name = name
        self.bullet_count = bullet_count

    def __str__(self):
        return "%s有%d发子弹" % (self.name,self.bullet_count)


class Soilder:

    def __init__(self,gun):
        self.gun = gun
        self.bullet = 10

    def __str__(self):
        return "士兵有一把 %s" % self.gun

    def fire(self,item):
        if self.bullet > 0:
            self.bullet = item.bullet_count - 1
            print('士兵拿着%s开火，子弹还剩：%d' % (item.name,self.bullet))
        else:
            print("%s已经没有子弹了，请装填子弹")

g = Gun("AK47",50)
print(g)

s = Soilder('')
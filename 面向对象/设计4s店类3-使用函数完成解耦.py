#coding:utf-8
__author__ = 'lc'



#coding:utf-8
__author__ = 'lc'

#coding:utf-8
__author__ = 'lc'

class CarStore(object):
    def order(self,cartype):
        select_by_cartype(cartype)

def select_by_cartype(self,cartype):
    if cartype == '名图':
        return Mingtu()
    elif cartype == '索纳塔':
        return Sonata()


class Car(object):
    def move(self):
        print('汽车在移动。。。。')

    def music(self):
            print('汽车在播放音乐。。。。')

    def stop(self):
            print('汽车停下了。。。。')

class Sonata():
    pass

class Mingtu():
    pass





c1 = CarStore()
car1 = c1.order('名图')
car1.move()
car1.music()
car1.stop()























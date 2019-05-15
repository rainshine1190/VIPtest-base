#coding:utf-8
__author__ = 'lc'

class CarStore(object):
    def order(self,money):
        if money > 5000:
            return Car()

class Car(object):
    def move(self):
        print('汽车在移动。。。。')

    def music(self):
            print('汽车在播放音乐。。。。')

    def stop(self):
            print('汽车停下了。。。。')


c1 = CarStore()
car1 = c1.order(6000)
car1.move()
car1.music()
car1.stop()





#coding:utf-8
__author__ = 'lc'

from threading import Thread
import time

g_num = 0


def test1():
    global g_num
    for i in range(1000000):
        g_num += 1
    print('test1计算后的值：',g_num)


def test2():
    global g_num
    for i in range(1000000):
        g_num += 1
    print('test2计算后的值：',g_num)



t1 = Thread(target=test1)
t1.start()

time.sleep(3)         #线程共享全局变量，有时候会发生问题，计算后不一致

t2 = Thread(target=test2)
t2.start()


print('最终值为：',g_num)


#问题：为什么g_num的值全局打印和test2打印的不一样




#答案：因为主线程在执行的时候，子线程也在同时执行，打印的那一瞬间取得是子线程执行过程中的某一瞬间的值
#可以通过让主线程等待的方式实现主线程的值为最终所有子线程执行后的值



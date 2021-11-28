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


t = []
t1 = Thread(target=test1)
t.append(t1)
t1.start()

# time.sleep(3)         #线程共享全局变量，有时候会发生问题，计算后不一致

t2 = Thread(target=test2)
t.append(t2)
t2.start()


for i in t:
    i.join()                    # 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生


print('最终值为：',g_num)














#coding:utf-8
__author__ = 'lc'

import threading
import time


def test(param):
    try:
        time.sleep(1)
        print(param)

    except Exception as msg:
        print('---',msg)


Mylist = [1,2,3,4,5]

for i in range(3):

    t = threading.Thread(target=test,args=(i,))
    t.start()


print('之前的线程数：',threading.activeCount())

while threading.activeCount() != 1: #当前线程数>1时，不停地循环；只剩下主线程，则会继续往下走
    pass

print('现在线程数：', threading.activeCount())







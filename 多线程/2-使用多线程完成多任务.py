#coding:utf-8
__author__ = 'lc'

import time
from threading import  Thread


##如果多个线程执行同意函数的话，各自之间互不影响，各是各的
def test(*param):
    print('-----昨晚喝多了，下次少喝点')
    # time.sleep(1)
    print('---',param[0])



for i in range(5):
    print('***',i)
    # test()
    #采用多线程修改
    t = Thread(target=test,args=(1,2))
    t.start()











#coding:utf-8
__author__ = 'lc'

import my_module1
import threading

class MyThread(threading.Thread):

    def run(self):
        for i in range(3):
            # time.sleep(1)
            #name属性保存的是当前线程的名字
            msg = "I'm "+self.name + ' @  ' + str(i)
            print(msg)

if __name__ == '__main__':
    t = MyThread()
    t.start()












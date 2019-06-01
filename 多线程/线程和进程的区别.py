#coding:utf-8
__author__ = 'lc'


#说明：全局变量和列表都可以让多线程共享


#全局变量出现问题的原因就是一行代码不会在CPU内一步执行完，有可能分多步，中间可能会执行其他线程的操作，造成多次执行
#数据错乱



from threading import Thread
import time


g_nums = [11,22,33]

def work1(nums):
    nums.append(44)
    print('test1计算后的值：',nums)


def work2(nums):
    time.sleep(1)
    print('test2计算后的值：',nums)



t1 = Thread(target=work1,args=(g_nums,))
t1.start()

# time.sleep(3)         #线程共享全局变量，有时候会发生问题，计算后不一致

t2 = Thread(target=work2,args=(g_nums,))
t2.start()


print('最终值为：',g_nums)








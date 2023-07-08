



from threading import Thread,Lock
import os,time

g_num = 1000000

def work1():
    global g_num

    # time.sleep(0.1)
    for i in range(500000):
        # 获取锁
        lock.acquire()
        g_num -= 1
        # 释放锁
        lock.release()
    print("in work1 g_num is : %d" % g_num)


def work2():
    global g_num
    for i in range(500000):
        # 获取锁
        lock.acquire()
        g_num -= 1
        # 释放锁
        lock.release()
    print("in work2 g_num is : %d" % g_num)


if __name__ == '__main__':
    lock = Lock()
    t1 = Thread(target=work1)
    t2 = Thread(target=work2)
    t1.start()
    # time.sleep(1)
    t2.start()
    t1.join()
    t2.join()
    print(f'最终的g_num：{g_num}')
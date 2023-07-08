



from threading import Thread,Lock
import os,time

g_num = 1000000

def work1():
    global g_num
    #获取锁
    lock.acquire()
    # time.sleep(0.1)
    for i in range(500000):
        g_num -= 1
    print("in work1 g_num is : %d" % g_num)
    #释放锁
    lock.release()

def work2():
    global g_num
    lock.acquire()
    for i in range(500000):
        g_num -= 1
    print("in work2 g_num is : %d" % g_num)
    lock.release()

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
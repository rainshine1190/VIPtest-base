import threading
import time

g_num = 1000000

def work1():
    global g_num
    for i in range(500000):
        g_num -= 1
    print("in work1 g_num is : %d\n" % g_num)

def work2():
    global g_num
    for i in range(500000):
        g_num -= 1
    print("in work2 g_num is : %d\n" % g_num)

if __name__ == '__main__':
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f'最终的g_num：{g_num}')


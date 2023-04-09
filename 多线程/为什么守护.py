"""
功能描述：
编写人：liangchao
编写日期：
实现逻辑：
导包
    1-
    2-
    3-

"""
import time,threading
def daemon_thread():
    for i in range(5):
        print('in Daemon the number is %d' % i)
        time.sleep(0.5)

def sub_thread():
    for i in range(5, 10):
        print(' in non-daemon the number is %d' % i)


t1 = threading.Thread(target=daemon_thread)
# t1 = threading.Thread(target=daemon_thread,daemon=True)
t1.setDaemon(True)

# t2 = threading.Thread(target=sub_thread)


t1.start()
# t2.start()


print('我结束了...')

#注意：
"""
线程创建默认非守护线程daemon=false
非守护线程不会跟着主线程结束而结束

守护线程会让子线程跟着主线程结束而结束

设置守护线程的方法：
创建线程时：daemon=True
创建线程后,启动前：t1.setDaemon=True

"""

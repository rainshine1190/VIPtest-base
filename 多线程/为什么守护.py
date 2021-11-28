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
        time.sleep(1)
        print('in Daemon the number is %d' % i)

def sub_thread():
    for i in range(5, 10):
        print(' in non-daemon the number is %d' % i)

t = threading.Thread(target=daemon_thread)
t1 = threading.Thread(target=sub_thread)
t.start()
t1.start()
t.join()
t1.join()

print('我结束了...')
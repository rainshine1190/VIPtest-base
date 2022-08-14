'''
1-导入包
2-定义多线程被执行函数
3-创建多线程
4-启动多线程
'''

import threading
import time

def run():
    """
    让多线程执行的方法
    :return:
    """
    # 获取当前线程的名称
    print(f"task-{threading.current_thread().getName()}")
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')

if __name__ == '__main__':
    # 创建线程
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run, name='threadt2')

    # 启动线程
    t1.start()
    t2.start()
    print('主线程结束了')

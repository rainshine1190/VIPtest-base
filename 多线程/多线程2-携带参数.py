'''
1-导入包
2-定义多线程执行函数
3-创建多线程
4-启动多线程
'''


import threading
import my_module1

def run(n):
    #获取当前线程的名称
    threadName = threading.current_thread().getName()
    print("task",threadName)
    my_module1.sleep(1)
    print('跑呀',n)
    my_module1.sleep(1)
    print('冲鸭',n)

if __name__ == '__main__':
    #多线程传参，注意如果是单个参数必须包含逗号（元组）
    t1 = threading.Thread(target=run, args=("t1",))
    t2 = threading.Thread(target=run, args=("t2",))
    t1.start()
    t2.start()

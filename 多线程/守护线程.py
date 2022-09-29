import threading
import time

def run(n):
    threadName = threading.current_thread().getName()
    print(f"task：{threadName} ")
    time.sleep(1)
    print(f'跑呀,{n} ')
    time.sleep(1)
    print(f'冲鸭,{n} ')

if __name__ == '__main__':
    # #第一种：让子线程跟着主线程一起结束，通过设置守护线程来实现（1-daemon传参；2-调用setDaemon）
    # t1 = threading.Thread(target=run, args=("t1",),daemon=True) #1-通过daemon传参设置守护线程
    # t1 = threading.Thread(target=run, args=("t1",))  # 1-通过daemon传参设置守护线程
    # t1.setDaemon(True)   #2-通过调用setDaemon把子进程设置为守护线程，必须在start()之前设置
    # t1.start()
    #第二种：让主线程等待子线程执行完，通过join阻塞主线程实现
    #
    # t2 = threading.Thread(target=run, name='thread-2',args=("t2",))
    # t2.start()
    # t2.join()            #设置主线程等待子线程
    print("主线程结束了")

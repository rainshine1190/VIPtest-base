import threading
import my_module1

def run(n):
    threadName = threading.current_thread().getName()
    print("task ",threadName)
    my_module1.sleep(0.5)
    print('跑呀',n)
    my_module1.sleep(1)
    print('冲鸭',n)

if __name__ == '__main__':
    t = threading.Thread(target=run, args=("t1",))
    t.setDaemon(True)   #把子进程设置为守护线程，必须在start()之前设置
    t.start()
    t.join()            #设置主线程等待子线程
    print("end")

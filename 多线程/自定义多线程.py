


import threading
import my_module1

class MyThread(threading.Thread):
    def __init__(self, n):
        super().__init__()  # 重构run函数必须要写
        self.n = n
        self.threadName = threading.current_thread().getName()

    def run(self):
        print("task", self.threadName)
        my_module1.sleep(1)
        print('跑呀%s'% self.n)
        my_module1.sleep(1)
        print('冲鸭%s'% self.n)

if __name__ == "__main__":
    t1 = MyThread("t1")
    t2 = MyThread("t2")
    t1.start()
    t2.start()

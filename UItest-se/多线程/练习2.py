#coding:utf-8
__author__ = 'lc'




from multiprocessing import Process
import os, my_module1

#计算密集型任务
def work():
    res = 0
    for i in range(100000000):
        res *= i

if __name__ == "__main__":
    l = []
    print("本机为",os.cpu_count(),"核 CPU")  # 本机为4核
    start = my_module1.time()
    for i in range(4):
        p = Process(target=work)  # 多进程
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop = my_module1.time()
    print("计算密集型任务，多进程耗时 %s" % (stop - start))








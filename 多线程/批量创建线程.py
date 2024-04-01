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


def run(i):
    print(threading.current_thread().getName(),f"---{i}")


if __name__ == '__main__':
    # 创建空列表用来存放线程对象
    tlist = []
    # 遍历创建线程，放入列表
    for i in range(100):
        t = threading.Thread(target=run,args=(i,))
        tlist.append(t)
    # 遍历列表，挨个启动
    for i in tlist:
        i.start()
    # 遍历列表，挨个阻塞
    for i in tlist:
        i.join()

    print('end')


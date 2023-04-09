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
    tlist = []
    for i in range(100):
        t = threading.Thread(target=run,args=(i,))
        tlist.append(t)

    for i in tlist:
        i.start()

    for i in tlist:
        i.join()

    print('end')

#coding:utf-8
__author__ = 'lc'



import requests,time
from threading import Thread

i = 0
n = 0


def http_get():
    global i,n
    url = "http://www.soho.com"
    # print('我是Thread%s' % Thread.getName(1))
    while True:
        re = requests.get(url=url)
        i += 1
        print(i)
        # # print('发送请求：%s次' % i)
        # if re.status_code == 200:
        #     n += 1
        #     # print('请求成功:%s次' % n)





# if __name__ == '__main__':

L = []

start_time = time.time()
for j in range(1000):

    t = Thread(target=http_get)
    print('------------------',j,t.name)

    # print()
    t.start()
    L.append(t)

for m in L:
    m.join()








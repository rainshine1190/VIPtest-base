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

import time
from multiprocessing import Pool
"""
apply : 阻塞调用函数，传递任意参数
apply_async: 不阻塞调用函数
"""
def test1(x, y):
    """执行脚本，执行过程需要等待2s"""
    print('~~~~')
    time.sleep(2)
    print( x + y)

def test2(x, y):
    """执行脚本，执行过程需要等待2s"""
    print('+++')
    time.sleep(2)
    print( x - y)

if __name__ == '__main__':
    n = 2
    #限制进程池进程数量
    pool = Pool(n)
    # apply(self, func, args=(), kwds={})
    # apply(self,func,*args,**kwds)
    # result = pool.apply(test, (2, 3), {'z': 1}) # 阻塞 主程序（主进程） 同步
    # res1 = pool.apply_async(test, (2, 3)) # 不阻塞 主程      异步

    re = []
    for i in range(n):
        res = pool.apply_async(test, (2, 3)) # 阻塞 主进程      同步
        re.append(res)
    for i in re:
        i.get()
    print("finished!")
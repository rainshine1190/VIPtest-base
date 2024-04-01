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
def test(x, y):
    """执行脚本，执行过程需要等待2s"""
    print('~~~~')
    time.sleep(2)
    print(f'{x} + {y}')

if __name__ == '__main__':
    n = 4
    #限制进程池进程数量
    pool = Pool(n)

    # # ------------创建单个子进程示例1：
    # # apply(self, func, args=(), kwds={})
    # # apply(self,func,*args,**kwds)
    # # pool.apply(test, (2, 3)) # 阻塞 主程序（主进程） 同步，无返回值
    # res1 = pool.apply_async(test, (2, 3)) # 不阻塞 主程 异步 返回异步结果对象
    # print("finished!")
    # # 阻塞函数不返回异步调用对象，不能调用回调函数：get方法
    # print(res1)
    # res1.get()

    # ------------创建批量子进程示例2：
    re = []
    #通过for循环建立多个子进程
    for i in range(5):
        res = pool.apply_async(test, (2, i))
        # pool.apply(test, (2, i))
        re.append(res)

    print("finished!")
    pool.close()
    pool.join()
    # 通过get方法获取执行结果
    # for i in re:
    #     i.get()
    #
    print("end!")


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
# def test(x, y):
#     """执行脚本，执行过程需要等待2s"""
#     print('~~~~')
#     time.sleep(2)
#     print(f'{x} + {y}')
#     return x,y
#
# def test1(x):
#     """执行脚本，执行过程需要等待2s"""
#     print('~~~~')
#     time.sleep(2)
#     print(f'{x}')
#     return x*2
#
# def call(result):
#     print(f'任务执行结束,结果是{result}')
#
# if __name__ == '__main__':
#     # n = 4
#     # #限制进程池进程数量
#     # pool = Pool(n)
#     #
#     # # ------------创建批量子进程示例2：
#     # re = []
#     # #通过for循环建立多个子进程
#     # for i in range(5):
#     #     res = pool.apply_async(test, (2, i),callback=call)
#     #     re.append(res)
#     #
#     # print("finished!")
#     #
#     # # 通过get方法获取执行结果
#     # for i in re:
#     #     res = i.get()
#     #     print(res)
#     #
#     # print("end!")
#     # 创建进程池，设置进程池大小
#     with Pool(processes=4) as pool:
#         # 使用进程池执行任务，这里的任务可以是一个可迭代对象，比如列表
#         results = pool.map_async(test1, [1, 2, 3, 4], callback=call)
#
#         # 等待所有任务完成
#         results.wait()
#
#         # 获取每个任务的结果
#         final_results = results.get()
#         print("Final results:", final_results)


from multiprocessing import Pool

def your_function(data):
    time.sleep(1)
    # 假设这里是你的任务处理函数
    return data * 2

def call(result):
    print(f'任务执行结束,结果是{result}')

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        results = pool.apply_async(your_function, [1, 2, 3, 4],callback=call)
        results.wait()
        final_results = results.get()
        print("Final results:", final_results)

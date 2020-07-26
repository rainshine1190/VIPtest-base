# try:
#     print(1/0)
# except ZeroDivisionError:
#     print('有错误')

# try:
#     print(1/0)
# except ZeroDivisionError as msg:
#     print(msg)



# try:
#     print(num)
# except Exception as msg:
#     print(msg)


# try:
#     print(a/2)
# except Exception as msg:
#     print(msg)
# else:
#     print('1/2执行了，且没有异常发生')
#
# finally:
#     print('程序执行了，不管异常还是正常')

#
# import time
# try:
#     f = open('test.txt')
#     try:
#         while True:
#             content = f.readline()
#             if len(content) == 0:
#                 break
#             time.sleep(2)
#             print(content)
#     except:
#         # 如果在读取⽂文件的过程中，产⽣生了了异常，那么就会捕获到
#         # ⽐比如 按下了了 ctrl+c
#         print('意外终⽌止了了读取数据')
#     finally:
#         f.close()
#         print('关闭⽂文件')
#         #向上层抛出异常
#         raise
# except:
#     print("没有这个⽂文件")


# import testA.my_module1 as t1
#
# # testA.my_module1 .test1()
# t1.test1()


from testA import my_module1

# testA.my_module1 .test1()
my_module1.test1()
import time


#等待n秒
time.sleep(2)
#获取当前时间戳
print(time.time())
#获取按照结构输出的时间格式，得到时间元组
print(time.localtime())
#按照指定的格式输出时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#将时间格式的字符串转换为时间元组，和strftime方法互逆
print(time.strptime('2021-07-25 14:27:28',"%Y-%m-%d %H:%M:%S"))




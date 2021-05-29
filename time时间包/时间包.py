import time



# time.sleep()
#获取当前时间戳
print(time.time())
#获取按照结构输出的时间格式
print(time.localtime())
#按照指定的格式输出时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


print('------')


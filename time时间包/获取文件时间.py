'''
功能描述：
编写人：
编写日期：

步骤分析：
    1-
    2-
    3-
'''
import os

#   os.getcwd() 方法用于返回当前工作目录
# 输出文件的创建时间
create_time =  os.path.getctime(__file__)
# 输出文件最近修改时间
modify_time =  os.path.getmtime(__file__)

print(create_time,modify_time)
"""
功能描述：
编写人：liangchao
编写日期：
实现逻辑：
    1-
    2-
    3-

"""

import configparser

# 1—	导入configparser
import configparser,os

# 2---实例化configparser一个对象，读取目标配置文件内容
conf = configparser.ConfigParser()
#读取文件的目录+文件名
# file_path = os.path.dirname("xxx/xxx")+("config.ini")
conf.read('config.ini',encoding="utf-8-sig")


# # 3---获取文件内的所有section
# sections = conf.sections()
# print('获取配置文件所有的section：',sections)

# 4---获取xx section下的所有option
options = conf.options('Mysql')
print('获取指定section下所有option', options)

# 5---获取xx section下的所有键值对
items = conf.items('Mysql')
print('获取指定section下所有的键值对', items)

# # 6—获取xx section下的某个option的value
value = conf.get('Mysql', 'host')
print('获取指定的section下的option', type(value), value)

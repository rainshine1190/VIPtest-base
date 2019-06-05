#coding:utf-8
__author__ = 'lc'



# 1—	导入configparser
import configparser,os


# 2---实例化configparser一个对象
conf = configparser.ConfigParser()


file = os.path.dirname(__file__) + "/" + "config.ini"
# print('file',file)

#3---读取config.ini文件
conf.read(file)


# 4---获取文件内的所有section
allSection = conf.sections()
print('获取配置文件所有的section', allSection)
#
# 5---获取xx section下的所有options
options = conf.options('mysql')
print('获取指定section下所有option', options)
#
# 6---获取xx section下的所有键值对
items = conf.items('mysql')
print('***',dict(items))
print('获取指定section下所有的键值对', items)
#
# 7—获取xx section下的某个option
value = conf.get('mysql', 'host')
print('获取指定的section下的option', type(value), value)









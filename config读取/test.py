"""
功能描述：
编写人：liangchao
编写日期：
实现逻辑：
    1-
    2-
    3-

"""

# -*- coding: utf-8 -*-
'''
@unittest    : 2021/3/6 14:13
@Author  : zxd
@功能:   配置文件读取方法
'''


import configparser, os

class ConfigRead():

    #属性
    def __init__(self):
        configfilepath = "config.ini"
        # print(configfilepath)
        #用来读取文件内容的对象
        self.conf = configparser.ConfigParser()
        self.conf.read(configfilepath, encoding="utf-8-sig")
    #读取email -section下的内容
    def readEmail(self, option="all"):
        config_json={}
        # 1.读取所有section
        # sects = self.conf.sections()
        # print(sects)
        # 2.读取所有options(名称)
        # opts = self.conf.options('Email')
        # print(opts)
        # 3.读取某个sections下的所有键值对
        # kvs = self.conf.items('app')
        # print(kvs)
        # 4.读取某个sections下的某个options
        # sov = self.conf.get('Email','smtpserver')
        # print(sov)
        if option == 'all':
            kvs = self.conf.items('App')
        print(kvs)
        print(len(kvs))
        for i in range(0,len(kvs)):
            print(f"这个是key{kvs[i][0]},这个是value{kvs[i][1]}")

            config_json[kvs[i][0]]=kvs[i][1]
        return kvs
if __name__ == '__main__':

    cr = ConfigRead()
    print(cr.readEmail())
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
# -*- coding: utf-8 -*-
# @Time:2022/4/30 17:45
# @Author: xiaodong

from locust import HttpUser,task
import logging
class point(HttpUser):
    @task
    def login(self):
        logging.captureWarnings(True)
        # palyed1 = {"email": "hyorg", "password": "1Q2w3e4r"}
        palyed2 = {"email": "org589", "password": "Abc12345"}
        response=self.client.post(f'/api/auth/login/',json=palyed2,verify=False)#https请求添加verify
        if response==200:
            print('登陆成功')
        else:
            print('登录失败')

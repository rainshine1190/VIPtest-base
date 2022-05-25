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

import pytest

@pytest.fixture()
def login():
	print("打开浏览器，登录成功")
	yield     #用例执行成功后执行，相当于teardown
	print("关闭浏览器")

def test(login):     #相当于setup在test用例前执行
	print("执行")

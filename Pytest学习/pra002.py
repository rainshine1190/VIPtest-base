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

@pytest.fixture(params=[1,2,3])
def login(request):          #传入参数params
	return request.param          #取列表中单个值

class test_A:
	def test_a(self,login):
		print("---------------------test_a")
		assert login !=3   #断言login不等于3

"""
功能描述：读取Excel的测试数据
编写人：
编写日期：
实现步骤：
    1-打开excel
    2-确定sheet页
    3-确定数据所在的行和列
    4-读取一行数据
    5-迭代读取所有行，放入列表
    6-返回目标数据


"""





#coding:utf-8
__author__ = 'lc'

import my_module1
from HTMLTestRunner import HTMLTestReportCN

from myfun import *

class myTest(my_module1.TestCase):

    def setUp(self):
        print('执行setup方法')

    def tearDown(self):
        print('执行tearDown方法')

    def test_add(self):
        self.assertEqual(add(1,2),3)

    def test_mul(self):
        self.assertEqual(multi(1,2),2)

if __name__ == "__main__":
    # 默认全部运行
    # unittest.main()
    #生成测试报告
    suite = my_module1.TestSuite()
    suite.addTest(myTest('test_add'))
    filename = "test.html"
    fp = open(filename,'wb')
    runner = HTMLTestReportCN(stream=fp, title='单元测试报告', description='我是描述')
    runner.run(suite)
    fp.close()

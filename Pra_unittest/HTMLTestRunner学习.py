#coding:utf-8
__author__ = 'lc'

import unittest,HTMLTestRunner
from myfun import *

class myTest(unittest.TestCase):

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
    suite = unittest.TestSuite()
    suite.addTest(myTest('test_add'))
    filename = "test.html"
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='单元测试报告', description='我是描述')
    runner.run(suite)
    fp.close()

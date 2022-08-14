#coding:utf-8
__author__ = 'lc'

import unittest
from Pra_unittest.myfun import *

#继承unittest.TestCase
class myTest(unittest.TestCase):

    def setUp(self):
        print('执行setup方法')

    def tearDown(self):
        print('执行tearDown方法')

    def test_add(self):
        print('执行test_add')
        #调用被测方法
        real = add(1,2)
        #断言实际结果和预期结果
        self.assertEqual(real,4,'两个参数不相等')

    def test_mul(self):
        print('执行test_mul')
        self.assertEqual(multi(1,2),2,'和预期不符')

if __name__ == "__main__":
    # 默认全部运行
    # unittest.main()
    #------------------------------testSuite示例
    #实例化testSuite
    suite = unittest.TestSuite()
    # #调用addTest方法
    suite.addTest(myTest('test_add'))
    suite.addTest(myTest('test_mul'))
    # #
    # print('suite内容：',suite)
    # #
    # #------------------------------testrunner示例
    runner = unittest.TextTestRunner()
    # # runner = unittest.TestRunner()
    runner.run(suite)


    #--------------------------------通过HtmlTestRunner运行并生成测试报告
    # suite = unittest.TestSuite()
    # suite.addTest(myTest('test_add'))
    # filename = "E:\\code\\VIPbase\\Pra_unittest\\test.html"
    # fp = open(filename,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='单元测试报告', description='我是描述')
    # runner.run(suite)
    # fp.close()

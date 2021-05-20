#coding:utf-8
__author__ = 'lc'

import my_module1,HTMLTestRunner
from myfun import *

class myTest(my_module1.TestCase):


    def setUp(self):
        print('执行setup方法')

    def tearDown(self):
        print('执行tearDown方法')

    def test_add(self):
        print('执行test_add')
        self.assertEqual(add(1,2),3)

    def test_mul(self):
        print('执行test_mul')
        self.assertEqual(multi(1,2),2)

if __name__ == "__main__":
    # 默认全部运行
    # unittest.main()
    #------------------------------testSuite示例
    #实例化testSuite
    suite = my_module1.TestSuite()
    #调用addTest方法
    suite.addTest(myTest('test_add'))

    print('suite内容：',suite)

    #------------------------------testrunner示例
    runner = my_module1.TextTestRunner()
    runner = my_module1.TestRunner()
    runner.run(suite)


    #--------------------------------通过HtmlTestRunner运行并生成测试报告
    # suite = unittest.TestSuite()
    # suite.addTest(myTest('test_add'))
    # filename = "E:\\code\\VIPbase\\Pra_unittest\\test.html"
    # fp = open(filename,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='单元测试报告', description='我是描述')
    # runner.run(suite)
    # fp.close()

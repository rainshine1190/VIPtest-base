#coding:utf-8

import unittest
from Pra_unittest.myfun import *

class TestMyFun(unittest.TestCase):

    # TestCase基类方法,所有case执行之前自动执行
    @classmethod
    def setUpClass(cls):
        print("这里是所有测试用例前的准备工作setUpClass")

    # TestCase基类方法,所有case执行之后自动执行
    @classmethod
    def tearDownClass(cls):
        print("这里是所有测试用例后的清理工作tearDownClass")

    # TestCase基类方法,每次执行case前自动执行
    def setUp(self):
        print("这里是一个测试用例前的准备工作setUp")

    # TestCase基类方法,每次执行case后自动执行
    def tearDown(self):
        print("这里是一个测试用例后的清理工作tearDown")


    def test_add(self):
        print('这里是运行的test开头的用例')
        result = add(1,2)
        self.assertEqual(3, result)
        # self.assertNotEqual(3, add(2, 2))  # 测试业务方法add

    @unittest.skipUnless(1<2,'这是跳过的原因/描述')
    def test_sub(self):
        print('这里跳过的用例')
        # self.assertEqual(3, add(1, 2))
        self.assertEqual(2,2,'预期和实际不一致，断言失败！')
        # self.assertNotEqual(3, add(2, 2))  # 测试业务方法add


if __name__ == '__main__':
    unittest.main(verbosity=2)



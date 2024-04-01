#coding:utf-8

import unittest

from Pra_unittest.myfun import *


# class TestA(unittest.TestCase):
#     b = 0
#
#     def testa(self):
#         b = 1
#         print(b)
#
# if __name__ == '__main__':
#     unittest.main()
#     print(TestA.b)
# a = TestA.b

a = 1
class TestMyFun(unittest.TestCase):
    # TestCase基类方法,所有case执行之前自动执行
    @classmethod
    def setUpClass(cls):
        print("这里是所有测试用例前的准备工作")

    # TestCase基类方法,所有case执行之后自动执行
    @classmethod
    def tearDownClass(cls):
        print("这里是所有测试用例后的清理工作")

    # TestCase基类方法,每次执行case前自动执行
    def setUp(self):
        print("这里是一个测试用例前的准备工作")

    # TestCase基类方法,每次执行case后自动执行
    def tearDown(self):
        print("这里是一个测试用例后的清理工作")

    @unittest.skip("我想临时跳过这个测试用例.")
    def test_add(self):
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))  # 测试业务方法add

    def test_minus(self):
        self.skipTest('跳过这个测试用例')
        self.assertEqual(1, minus(3, 2))  # 测试业务方法minus
    def test_multi(self):
        self.assertEqual(6, multi(2, 3))  # 测试业务方法multi

    @unittest.skipUnless(a>0,'tiaojian')
    def test_divide(self):
        # print(self.b)
        self.assertEqual(2, divide(6, 3))  # 测试业务方法divide
        self.assertEqual(2.5, divide(5, 2))

    @unittest.skipIf(a>0,'条件通过')
    def test_skip(self):
        print('我被跳过了')
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main(verbosity=1)



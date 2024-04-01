#coding:utf-8

import unittest
from myfun import *



class Testfun1(unittest.TestCase):

    def test_add(self):
        print('执行add')
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))  # 测试业务方法add

    def test_bminus(self):
        print('执行minus')
        # self.skipTest('跳过这个测试用例')
        self.assertEqual(1, minus(3, 2))  # 测试业务方法minus

class Testfun2(unittest.TestCase):

    def test_multi(self):
        print('执行multi')
        self.assertEqual(6, multi(2, 3))  # 测试业务方法multi
    def test_divide(self):
        self.assertEqual(2, divide(6, 3))  # 测试业务方法divide
        self.assertEqual(2.5, divide(5, 2))


if __name__ == '__main__':
    unittest.main()
    # # unittest.main(verbosity=2)
    # #创建测试套件suite1--添加Testfun1单元测试类中的被测方法
    suite1 = unittest.TestSuite()
    suite1.addTest(Testfun1("test_bminus"))
    # #创建测试套件suite2--添加Testfun2单元测试类中的被测方法
    # suite2 = unittest.TestSuite()
    # suite2.addTest(Testfun2("test_multi"))
    #
    # print('***',suite1,suite2)
    # #创建总测试套件，依次添加测试套件suite1和suite2，相当于把Testfun1和Testfun2中的所有测试方法汇总
    # suite = unittest.TestSuite()
    # suite.addTests((suite1,suite2))
    # # suite.addTests(suite2)
    # print('---',suite)
    #
    # #运行总的测试套件
    runner = unittest.TextTestRunner()
    runner.run(suite1)

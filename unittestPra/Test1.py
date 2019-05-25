#coding:utf-8
__author__ = 'lc'


import unittest
from unittestPra import Mysum


class testMy(unittest.TestCase):

    def setUp(self):
        print('---初始化测试环境')


    def test_sum(self):
        x = int(input('>---'))
        y = int(input('>---'))
        re = Mysum.add(x,y)
        if re == 3:
            print('测试通过')
        else:
            print('测试失败')

    def tearDown(self):
        print('---清理测试环境')





if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(testMy.test_sum())
    # runner = unittest.TextTestRunner()
    # runner.run(suite)







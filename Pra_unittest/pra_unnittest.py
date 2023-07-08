#coding:utf-8
# __author__ = 'lc'
'''
功能：
    1.讲解unittest使用
        a-test开头的方法
        b-setUp和teardown方法
        c-setUpClass和tearDownClass
'''


import unittest
from Pra_unittest.myfun import *


#继承unittest.TestCase
class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\nsetUpClass方法，所有用例执行前一共执行一遍')

    #每条test开头的用例方法执行前必须执行一遍
    def setUp(self):
        print('执行setUp方法')

    def test_add1(self):
        print('------执行add1方法')
        real = add(1,2)
        self.assertEqual(real,3)

    def test_add2(self):
        print('------执行add2方法')
        real = add(-1, 2)
        try:
            self.assertEqual(real,1)
        except AssertionError as msg:
            print(msg)

    #每条test开头的用例方法执行后必须执行一遍
    def tearDown(self):
        print('执行teardown')
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass方法，所有用例执行后一共执行一遍')

# print('*******',__name__)
if __name__ == '__main__':
    print('----------------------------------')
    # unittest.main()
    suite = unittest.TestSuite()
    # suite.addTest(MyTest('test_add1'))
    # suite.addTest(MyTest('test_add2'))
    suite.addTests((MyTest('test_add1'),MyTest('test_add2')))
    print('---suite', suite)
    runner = unittest.TextTestRunner()
    runner.run(suite)



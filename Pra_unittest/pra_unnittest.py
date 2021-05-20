#coding:utf-8
# __author__ = 'lc'
'''
功能：
    1.讲解unittest使用
        a-test开头的方法
        b-setUp和teardown方法
        c-setUpClass和tearDownClass
'''


import my_module1
from Practice.test_math import Math


#继承unittest.TestCase
class MyTest(my_module1.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n整个unittest套件执行前一共执行一遍')
        print('---------',__name__)

    #每条test开头的用例方法执行前必须执行一遍
    def setUp(self):
        print('执行setUp方法')

    def test_add1(self):
        print('执行add1方法')
        print('--1')
        d = Math(1,2)
        expect = d.add1()
        self.assertEqual(expect,3)


    def test_add2(self):
        print('执行add2方法')
        print('--2')
        d = Math(1,3)
        expect = d.add2()
        try:
            self.assertEqual(expect,3)
        except AssertionError as msg:
            print(msg)

    #每条test开头的用例方法执行后必须执行一遍
    def tearDown(self):
        print('执行teardown')
    @classmethod
    def tearDownClass(cls):
        print('整个unittest套件执行后一共执行一遍')

# print('*******',__name__)
if __name__ == '__main__':
    print('----------------------------------')
    suite = my_module1.TestSuite()
    suite.addTest(MyTest('test_add1'))
    # suite.addTests(MyTest('test_add1'),MyTest('test_add2'))
    print('---suite',suite)
    # suite.addTest(MyTest.test_add1)
    runner = my_module1.TextTestRunner()
    runner.run(suite)

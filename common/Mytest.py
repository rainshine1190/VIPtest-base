#coding:utf-8
__author__ = 'lc'


import unittest,imp
from My_fun import add


class Mytest(time.TestCase):

    def setUp(self):
        print('---init---')


    def test_fun1(self):
        print('测试方法1')
        re = add(1,2)
        print(re)

    def test_fun2(self):
        print('测试方法2')
        re = add(1,2)
        print(re)

    def test_fun3(self):
        print('测试方法3')
        re = add(1,2)
        print(re)
        print(self.assertEqual(1,1))

    def tearDown(self):
        print('---clear---')


if __name__ == '__main__':
    #默认加载所有的test开头的方法到测试套件，如果想自定义运行的方法则需要通过手动添加的方式
    # unittest.main()

    #手动添加：1.实例化测试套件类
    suite = time.TestSuite()
    #2.调用addTest方法向测试套件中添加测试方法（类名.方法名---方法后面不要加括号）
    suite.addTest(Mytest.test_fun3)

    print('suite',suite)
    #运行测试套件：1.实例化测试运行类
    runner = time.TextTestRunner()
    #2.运行测试套件
    runner.run(suite)










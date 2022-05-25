
import unittest
from myfun import *
import test_fun

class myTest(unittest.TestCase):

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
    #------------------------------1-全部的执行方法
    # unittest.main()

    #------------------------------2-使用testSuite添加指定方法执行
    #1-实例化testSuite
    suite = unittest.TestSuite()
    #2-调用addTest方法
    # suite.addTest(myTest('test_add'))
    suite.addTest(myTest('test_mul'))
    #加入其他模块的test方法
    # suite.addTest(test_fun.myTest('test_mul'))
    #加入多个test开头的方法
    # suite.addTests((myTest('test_add'),myTest('test_mul')))
    #查看suite的内容
    print('suite内：',suite)

    #执行测试套件
    #1-实例化
    runner = unittest.TextTestRunner()
    # #2-调用run方法
    runner.run(suite)
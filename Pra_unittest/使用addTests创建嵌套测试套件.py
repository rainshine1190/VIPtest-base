#coding:utf-8

import my_module1
from myfun import *



class Testfun1(my_module1.TestCase):

    def test_add(self):
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))  # 测试业务方法add

    def test_minus(self):
        self.skipTest('跳过这个测试用例')
        self.assertEqual(1, minus(3, 2))  # 测试业务方法minus

class Testfun2(my_module1.TestCase):

    def test_multi(self):
        self.assertEqual(6, multi(2, 3))  # 测试业务方法multi
    def test_divide(self):
        self.assertEqual(2, divide(6, 3))  # 测试业务方法divide
        self.assertEqual(2.5, divide(5, 2))


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    #创建测试套件suite1--添加Testfun1单元测试类中的被测方法
    suite1 = my_module1.TestSuite()
    suite1.addTest(Testfun1("test_minus"))
    #创建测试套件suite2--添加Testfun2单元测试类中的被测方法
    suite2 = my_module1.TestSuite()
    suite2.addTest(Testfun2("test_multi"))

    print('***',suite1,suite2)
    #创建总测试套件，依次添加测试套件suite1和suite2，相当于把Testfun1和Testfun2中的所有测试方法汇总
    suite = my_module1.TestSuite()
    suite.addTests(suite1)
    suite.addTests(suite2)
    print('---',suite)

    #运行总的测试套件
    runner = my_module1.TextTestRunner()
    runner.run(suite)

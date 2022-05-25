#coding:utf-8
__author__ = 'lc'




import  unittest
from ddt import ddt,data,unpack

list1 = [5,6,7]

@ddt
class Mytest1(unittest.TestCase):
    #单次执行，传递单个参数（该方法一共执行一遍）
    @data(1)
    def test_bb1(self,value):
        print(value)
        self.assertEqual(value,2)

    #多次执行，传递单个参数（该方法一共执行3遍；第一次传2；第二次传3,；第三次传4，）
    @data(2,3,4)
    def test_bb2(self,value):
        print(value)
        self.assertEqual(value, 2)

    #可变参数，通过*args传递，传递方式同上（该方法执行次数由参数的元素个数决定）
    @data(*list1)
    def test_bb3(self,value):
        print(value)
        self.assertEqual(value, 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)






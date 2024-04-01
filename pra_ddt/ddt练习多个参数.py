#coding:utf-8
__author__ = 'lc'




import  unittest
from ddt import ddt,data,unpack

test_data = [[1,2],[3,4]]

@ddt
class Mytest1(unittest.TestCase):
    #单次执行，单次传递多个参数（一共执行一次，第一次传递两个参数）
    @data((1,1))
    @unpack
    def test_bb1(self,value1,value2):
        print('---',value1,value2)
        self.assertEqual(value1,value2)

    #多次执行，单次传递多个参数（一共执行两次，第一次传递两个参数1和2；第二次传递3和3）
    @data([1,2],[3,3])
    @unpack
    def test_bb2(self,value1,value2):
        print('+++',value1,value2)
        self.assertEqual(value1,value2)

    #多次执行，单次传递多个参数（一共执行两次，第一次传递两个参数1和2；第二次传递3和4）
    @data(*test_data)
    @unpack
    def test_bb3(self,value1,value2):
        print('===',value1,value2)
        self.assertEqual(value1,value2)

if __name__ == '__main__':
    unittest.main(verbosity=2)








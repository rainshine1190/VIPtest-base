#coding:utf-8
__author__ = 'lc'




import  unittest

from ddt import ddt,data,unpack


@ddt
class Mytest1(unittest.TestCase):

    @data(1)
    def test_bb1(self,value):
        print(value)
        self.assertEqual(value,2)

    @data(2,3,4)
    def test_bb2(self,value):
        print(value)
        self.assertEqual(value, 2)



if __name__ == '__main__':
    unittest.main()






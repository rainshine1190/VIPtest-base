#coding:utf-8
__author__ = 'lc'




import  unittest

from ddt import ddt,data,unpack



@ddt
class Mytest1(unittest.TestCase):

    @data((1,1),(3,4))
    @unpack
    def test_bb1(self,value1,value2):
        print('---',value1,value2)
        self.assertEqual(value1,value2)

    @data([1,2],[3,3])
    @unpack
    def test_bb2(self,value1,value2):
        print('---',value1,value2)
        self.assertEqual(value1,value2)


    @data({'value1':1,'value2':1},{'value1':3,'value2':4})
    @unpack
    def test_bb3(self,value1,value2):
        print('---',value1,value2)
        self.assertEqual(value1,value2)


if __name__ == '__main__':
    unittest.main()






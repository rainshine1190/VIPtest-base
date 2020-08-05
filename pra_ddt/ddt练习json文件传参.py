
import unittest
from ddt import ddt,data,unpack,file_data

@ddt
class TestMy(unittest.TestCase):

    @file_data('D:\\code\\VIPtest2\\pra_ddt\\data.json')
    def test_fun(self,value):
        print(value)

if __name__ == '__main__':
    unittest.main()
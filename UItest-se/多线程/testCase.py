


import my_module1
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ddt import ddt,data,unpack
import testData

import sys  #引入模块
str1= sys.argv[1:3]
print('str1---',str1)



class testCase(my_module1.TestCase):

    # testdata = testData.fun()
    # print(testdata)


    def test_interface(self):
        print('test_interface',str1)




if __name__ == '__main__':
    my_module1.main()
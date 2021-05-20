
import my_module1
from ddt import ddt,data,unpack,file_data

@ddt
class TestMy(my_module1.TestCase):

    @file_data('D:\\code\\VIPbase\\pra_ddt\\data.json')
    def test_fun(self,value):
        print(value)

if __name__ == '__main__':
    my_module1.main()
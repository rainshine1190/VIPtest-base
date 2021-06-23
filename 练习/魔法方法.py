"""
功能描述：
编写人：liangchao
编写日期：
实现逻辑：
    1-
    2-
    3-

"""
#创建类
class Washer():

    def __init__(self,height,width):
        self.height = height
        self.width = width

    #方法
    def wash(self):
        # print(self)

        print('洗衣服')

    def print_info(self):
        print('类里面获取对象的属性', self.height)
        print('类里面获取对象的属性', self.width)

    # def __str__(self):
    #     return f'这是高度：{self.height}宽度：{self.width}海尔洗衣机的使用说明书'

    def __del__(self):
        print(f'{self}被删除了')

hair1 = Washer(10,5)
# print('hair1的height为',hair1.height)

# hair1.print_info()

# print(hair1)


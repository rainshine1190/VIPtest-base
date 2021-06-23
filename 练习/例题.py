"""
功能描述：
编写人：liangchao
编写日期：
实现逻辑：
类：地瓜类
    1-地⽠瓜的属性
        被烤的时间 cooktime = 0
        地⽠瓜的状态 status = '生的'
        添加的调料料 condiments = []
    2-地⽠瓜的⽅方法
        2.1-被烤 cook，入参：烤的时间
            ⽤用户根据意愿设定每次烤地⽠瓜的时间
            判断地⽠瓜被烤的总时间是在哪个区间，修改地⽠瓜状态
            0-3分钟：⽣生的 if 0<=cooktime<3:
                                self.status = '生的'
            3-5分钟：半⽣生不不熟
                            if 3<=cooktime<5:
                                self.status = '半⽣生不不熟'
            5-8分钟：熟的
            超过8分钟：烤糊了了

        2.2-添加调料料 add condiments，入参：cordiments
            ⽤用户根据意愿设定添加的调料料
            将⽤用户添加的调料料存储
            self.cordiments.append()

        2.3-显示对象信息
            __str__(self):
                return f'地瓜烤了self.cooktime,地瓜现在是self.status,地瓜现在的调料有：self.cordiments


"""

class Tomato():

    def __init__(self):
    # 1-地⽠瓜的属性
    #     被烤的时间 cooktime = 0
        self.cooktime = 0
    #     地⽠瓜的状态 status = '生的'
        self.status = '生的'
    #     添加的调料料 condiments = []
        self.cordiments = []

    def cook(self,time):
        """
                2.1-被烤 cook，入参：烤的时间
            ⽤用户根据意愿设定每次烤地⽠瓜的时间
            判断地⽠瓜被烤的总时间是在哪个区间，修改地⽠瓜状态
            0-3分钟：⽣生的 if 0<=cooktime<3:
                                self.status = '生的'
            3-5分钟：半⽣生不不熟
                            if 3<=cooktime<5:
                                self.status = '半⽣生不不熟'
            5-8分钟：熟的
            超过8分钟：烤糊了了
        :return:
        """
        self.cooktime = self.cooktime + time
        if 0<= self.cooktime <3:
            self.status = '生的'
        elif 3 <= self.cooktime < 5:
            self.status = '半⽣生不不熟'
        elif 5 <= self.cooktime < 8:
            self.status = '熟了'
        elif 8 <= self.cooktime :
            self.status = '糊了'


    def add_cordiments(self,item):
        """
            ⽤用户根据意愿设定添加的调料料
            将⽤用户添加的调料料存储
            self.cordiments.append()
        :return:
        """
        self.cordiments.append(item)


    def __str__(self):
        return f'地瓜烤了{self.cooktime}分钟,地瓜现在是{self.status},地瓜现在的调料有：{self.cordiments}'



if __name__ == '__main__':
    t = Tomato()
    print(t)
    t.cook(2)
    print(t)
    t.cook(3)
    print(t)
    t.add_cordiments('孜然')
    t.add_cordiments('酱油')
    print(t)
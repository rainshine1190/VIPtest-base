"""
功能描述：

需求主线：
1. 被烤的时间和对应的地⽠瓜状态：
0-3分钟：⽣生的
3-5分钟：半⽣生不不熟
5-8分钟：熟的
超过8分钟：烤糊了了

2. 添加的调料料：
⽤用户可以按⾃自⼰己的意愿添加调料料


编写人：liangchao
编写日期：
实现逻辑：

类：地瓜

属性：
状态 status
被烤的时间 int
添加的调料 list

方法：
烤
根据烤地瓜的时间判断地瓜所处的状态
if -elif
0-3分钟：⽣生的
3-5分钟：半⽣生不不熟
5-8分钟：熟的
超过8分钟：烤糊了了

添加调料
接受用户添加的调料得出地瓜的口味，list

"""

class Potato():
    # 属性：

    def __init__(self):
        self.status = '生的'
        self.time = 0
        self.condiments = []
    #
    # 方法：
    def cook(self,time):
        #烤地瓜的状态是由累计烤的时间来决定的，而非每次烤的时间
        self.time += time
        if self.time < 3:
            self.status = '生的'
        elif 3<= self.time < 5:
            self.status = '半生不熟'
        elif 5<= self.time <= 8:
            self.status = '熟了'
        elif self.time > 8:
            self.status = '糊了'

    def add_codiments(self,item):
        self.condiments.append(item)

    def __str__(self):
        return f'地瓜被烤了{self.time}分钟，目前的状态是：{self.status},现在的口味是{self.condiments}'

#实例化
p = Potato()
print(p)

p.cook(2)
print(p)
p.cook(2)
print(p)
p.cook(2)

p.add_codiments('五香')
p.add_codiments('麻辣')

print(p)

#coding:utf-8
# __author__ = 'lc'


def person(name,age,**kwargs):
    print('****',name,age,kwargs)


person('xiaoming',21,sex='male',color='blue')
person('xiaoming',21)
person('xiaoming',21,sex=1)
# person('xiaoming',21,'male')

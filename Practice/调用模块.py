#coding:utf-8
# __author__ = 'lc'

#只能导入模块名
import Mymodule




#如果通过import调用，使用包内的方法需要通过包名.函数名的形式
Mymodule.fun1()

#--------------------------------------------------------------
#通过from。。。import形式导入，注意：from后面只能跟包和模块名，import后面跟函数名或类名
from Mymodule import fun1

#通过import * 可以导入全部函数
from Mymodule import *

#通过from-import的形式可以直接使用函数名
fun1()
fun2()

#------------------------------------------------------------



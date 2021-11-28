"""
功能描述：
编写人：liangchao
编写日期：
实现逻辑：
导包
    1-确定excel的位置
    2-打开excel
    3-确定sheet页
    4-确定数据的最大行
    5-读取全部数据
        for循环实现

"""
import xlrd


# 1 - 确定excel的位置

# 2 - 打开excel
wb = xlrd.open_workbook('data.xls')
# 3 - 确定sheet页
sh = wb.sheet_by_index(0)
# 4 - 确定数据的最大行
rown = sh.nrows
# 5 - 读取全部数据
# data = sh.row_values()
# for循环实现
data = []
for i in range(rown):
    d = sh.row_values(i)
    data.append(d)


print(data)
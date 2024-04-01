"""
功能描述：
编写人：liangchao
编写日期：
实现逻辑：
导包
    1-
    2-
    3-

"""
import time

from selenium import webdriver
from PIL import ImageGrab

# driver = webdriver.Chrome()
# driver.get('https://www.zhipin.com/beijing/?sid=sem_pz_bdpc_dasou_title')
# time.sleep(30)
#
# time.sleep(100)


# 指定要截图的区域（左上角坐标和右下角坐标）
left = 400  # 左上角 x 坐标
top = 0   # 左上角 y 坐标
right = 1500 # 右下角 x 坐标
bottom = 800 # 右下角 y 坐标

time.sleep(5)

# 截取指定区域的截图
screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

# 保存截图为文件
screenshot.save("screenshot2.png")

# 显示截图（可选）
screenshot.show()

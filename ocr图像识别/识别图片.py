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
import pytesseract
from PIL import Image

# 打开图像文件
image = Image.open('pillow.png')

# 使用Tesseract进行OCR识别
text = pytesseract.image_to_string(image,lang='eng')

# 输出识别的文本
print(text)

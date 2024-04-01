import time,re

import pytesseract
from PIL import Image

start = time.time()
# 打开图像文件
image = Image.open("screenshot2.png")

# 使用用户词库
custom_words_file = "user-words.txt"
custom_config = f"--user-words {custom_words_file}"

# 使用 pytesseract 提取文本
# text = pytesseract.image_to_string(image, lang='chi_sim',config=custom_config)
text = pytesseract.image_to_string(image, lang='eng',config=custom_config)

# 输出提取到的文本
print(text)
pattern = re.compile(r'((13[0-9]|14[5-9]|15[0-3,5-9]|16[6]|17[0-8]|18[0-9]|19[1,5,8,9])\d{8})(?!@)')

list1 = pattern.findall(text)
for x,y in list1:
    if len(x) == 11:
        print(x)
    else:print(y)


end = time.time()
elapse = end-start
print(elapse)
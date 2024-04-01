import cv2
import pytesseract

# 用OpenCV加载图像
image = cv2.imread("pillow.png")



# 转换图像为灰度
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 对灰度图像进行二值化处理
thresh = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# 去除图像中的噪声
noise_reduced_image = cv2.fastNlMeansDenoising(thresh, None, 10, 7, 21)

# 使用Tesseract提取文本
text = pytesseract.image_to_string(noise_reduced_image)

# 输出提取到的文本
print(text)

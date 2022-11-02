# 裁剪
import cv2

image = cv2.imread("opencv_logo.jpg")

# 先y轴再x轴
crop = image[10:170, 40:200]

cv2.imshow("crop", crop)
cv2.waitKey()

# 均值滤波
import cv2

image = cv2.imread("plane.jpg")

# 高斯滤波器GaussianBlur，高斯内核为五个像素，
gauss = cv2.GaussianBlur(image, (5, 5), 0)

# 中值滤波器，内核为五个像素
median = cv2.medianBlur(image, 5)

cv2.imshow("image", image)
cv2.imshow("gauss", gauss)
cv2.imshow("median", median)

cv2.waitKey()


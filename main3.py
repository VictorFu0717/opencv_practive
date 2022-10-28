import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8) #建一個二維陣列
kernel2 = np.ones((5,5), np.uint8) #建一個二維陣列

img = cv2.imread('cat.jpeg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #轉換成灰階圖片
blur = cv2.GaussianBlur(img, (15,15), 10) # 模糊圖片, 第二個參數為核大小(5,5)為5x5 只能放奇數, 第三個參數放標準差, 第二和三參數越大圖片越模糊
canny = cv2.Canny(img, 100, 150) #canny:找邊緣,看像素點和周圍的像素差別很大,就判別為邊緣 第二參數：最低門檻值, 第三參數：最高門檻值
dilate = cv2.dilate(canny, kernel, iterations=1) #膨脹, 第二個參數要放核大小（二維陣列）, 第三個參數放膨脹幾次, 值越大線條越粗
erode = cv2.erode(dilate, kernel2, iterations=1) #侵蝕, 讓線條變細

# cv2.imshow('img', img)
# cv2.imshow('gray', gray)
# cv2.imshow('blur', blur)
cv2.imshow('canny', canny)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)
cv2.waitKey(0)
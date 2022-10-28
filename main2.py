import cv2
import numpy as np
import random
# B  G  R
# 藍 綠  紅

img = cv2.imread('cat.jpeg')
# print(img.shape)

# img = np.empty((300, 300, 3), np.uint8) # np.empty創建多維陣列 , 8:8bit, uint:正整數
#
# for row in range(300):
#     for col in range(img.shape[1]):
#         img[row][col] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

new_img = img[:150,:300]

cv2.imshow('img',img)
cv2.imshow('new_img',new_img)
cv2.waitKey(0)
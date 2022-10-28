# 人臉偵測 opencv github -> data -> haarcascades 有訓練好的模型
import cv2
import numpy as np

img = cv2.imread('face.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier('/Users/victor/PycharmProjects/venv/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml') #載入訓練好的模型
faceRect = faceCascade.detectMultiScale(gray, 1.2, 3) # 參2:圖片縮小的倍數, 參3:整張圖片要偵測幾次
print(len(faceRect))

for (x, y, w, h) in faceRect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
#輪廓檢測
import cv2

img = cv2.imread('cat.jpeg')
imgContour = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img, 100, 150)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #RETR_EXTERNAL偵測外輪廓, CHAIN_APPROX_NONE不做壓縮

for cnt in contours:
    cv2.drawContours(imgContour, cnt, -1, (255,0,0), 4) #畫出輪廓
    print(cv2.contourArea(cnt)) #算出輪廓面積
    print(cv2.arcLength(cnt, False)) #印出輪廓邊長; 2:輪廓是否為閉合的True/False

cv2.imshow('img', img)
cv2.imshow('canny', canny)
cv2.imshow('imgContour', imgContour)
cv2.waitKey(0)
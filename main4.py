import cv2
import numpy as np
img = np.zeros((600, 600, 3), np.uint8) #創建RGB皆為0的圖片：黑色
cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0), 2) #畫一條直線, 第2參數起始點座標, 第3參數終點座標, 連成直線; 第四參數為顏色 ;第五參數為線條粗度
cv2.rectangle(img, (0,0), (400,300), (0,0,255), cv2.FILLED) #畫出方形, cv2.FILLED為填滿顏色
cv2.circle(img, (300, 400), 40, (255, 0, 0), 2) #畫圓形, 第二參數為圓心座標, 第三參數為半徑
cv2.putText(img, 'Hello', (100,500), cv2.FONT_HERSHEY_SIMPLEX, 2, (250, 250, 250), 2) #不支援寫中文, 3:文字左下角座標, 4:字體, 5:文字大小, 6：粗度


cv2.imshow('img',img)
cv2.waitKey(0)
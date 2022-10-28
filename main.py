import cv2

# img = cv2.imread('cat.jpeg') #讀取圖騙路徑
#
# #img = cv2.resize(img,(300,300)) #改變圖片大小
# img = cv2.resize(img,(0,0), fx=0.5, fy=0.5) #寬度和高度變成0.5倍
# cv2.imshow('cat',img)
# cv2.waitKey(2000) #等待一秒, "0" 顯示無限久

cap = cv2.VideoCapture('https://admin:Nadi1234;@192.168.3.98:7001/media/e8be3ddd-35d3-b0e4-406e-086f9501bce5.webm') # 可放影片路徑（'cat_video.mp4'）or 0 鏡頭

while True:
    ret, frame = cap.read() # ret :boolean表示下是否讀取成功, frame: 如果成功回傳下一楨
    # frame = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5)
    if ret:
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break






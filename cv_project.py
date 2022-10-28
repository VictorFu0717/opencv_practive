import cv2



cap = cv2.VideoCapture(0) # 可放影片路徑（'cat_video.mp4'）or 0 鏡頭

while True:
    ret, frame = cap.read() # ret :boolean表示下是否讀取成功, frame: 如果成功回傳下一楨
    if ret:
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break


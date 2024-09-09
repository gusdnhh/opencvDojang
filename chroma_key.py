import sys
import numpy as np
import cv2

def on_trackbar_S(pos):
    global smin, smax
    smin = cv2.getTrackbarPos('S_min', 'frame')
    smax = cv2.getTrackbarPos('S_max', 'frame')    


# 동영상 파일명
fileName1 = 'data2/woman.mp4'
fileName2 = 'data2/raining.mp4'

# 영상 불러오기
cap1 = cv2.VideoCapture(fileName1)
cap2 = cv2.VideoCapture(fileName2)

if not cap1.isOpened():
    sys.exit("video1 open failed")  
if not cap2.isOpened():
    sys.exit("video2 open failed")
    
    
fps1 = int(cap1.get(cv2.CAP_PROP_FPS))

# 초당 몇프레임 : 1번 동영상 기준
delay = int(1000/fps1)



# 합성 여부 설정 플레그
do_composite = False

ret1, frame1 = cap1.read()

cv2.imshow('frame', frame1)
cv2.createTrackbar('S_min', 'frame', 140, 255, on_trackbar_S)
cv2.createTrackbar('S_max', 'frame', 150, 255, on_trackbar_S)

while True:
    ret1, frame1 = cap1.read()
    if not ret1:
        break
    
    if do_composite:
        ret2, frame2 = cap2.read()
        if not ret1:
            break
    
        # hsv 색공간에서 영역을 검출해서 합성
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        # h : 50~70, s : 150~255, v : 0~255
        mask = cv2.inRange(hsv, (50,smin,0),(70,smax,255))
        cv2.copyTo(frame2, mask, frame1)
    
    # 결과 확인
    cv2.imshow('frame', frame1)
    
    key = cv2.waitKey(delay)

    # 스페이스 바를 눌렀을 때 do_composite를 반전
    if key == ord(' '):
        do_composite = not do_composite
    # ESC가 입력되면 종료
    elif key == 27:
        break
    
cap1.release()
cap2.release()
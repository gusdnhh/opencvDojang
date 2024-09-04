# 이미지를 불러올 때는 imread()
# 동영상을 불러올 떄는 VideoCapture()

import cv2, sys

fileName = 'data/data/vtest.avi'

# videocapture 클래스 객체 생성 + 생성자가 호출(파일읽기)
cap = cv2.VideoCapture(fileName)

# 동영상의 해상도 width, height를 확인
frameSize = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) , int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(frameSize)


# 동영상 이미지를 다 가져올 때까지 반복
while True:
    # 동영상에서 한장의 이미지를 가져오기
    
    # retval : 동영상에서 이미지 가져올 떄 정상 동작 하였는가?
    # frmae : 이미지 한장
    # 동영상 코덱 디코딩도 포함
    retval, frame = cap.read()
    
    # retval가 양수가 아니면 while문 빠져나가기(종료)
    if not retval:
        break
    
    cv2.imshow('frame', frame)
    
    # 100ms 대기 / (이 동영상은 초당 10프레임 짜리니까)
    key = cv2.waitKey(100)
    
    if key == 27:
        break
    
if cap.isOpened():
    cap.release() # 열림 해제
    
cv2.destroyAllWindows()

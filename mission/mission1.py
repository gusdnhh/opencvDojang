import cv2
import numpy as np

# 전역 변수들
shift_down = False
polyPt = []

def mouse_callback(event, x, y, flags, param):
    global polyPt, shift_down, img
    
    # 마우스 오른쪽 버튼으로 원을 그리기
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 70, (255, 0, 0), 1)
    
    # Shift 키가 눌린 상태에서 마우스 왼쪽 버튼 클릭
    elif event == cv2.EVENT_LBUTTONDOWN and shift_down:
        polyPt.append((x, y))
        print(polyPt)
    

# 빈 이미지 생성
img = np.zeros((512, 512, 3), dtype=np.uint8) + 255

cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

while True:
    cv2.imshow('image', img)
    
    key = cv2.waitKey(10) & 0xFF
    
    # Shift 키 감지
    if key == ord('a'):  # Shift 키가 눌림
        shift_down = True
    elif key == ord('s'):  # 키가 눌리지 않았을 때 (OpenCV에서는 -1이 나옴)
        shift_down = False
    elif key == 27:  # 'esc'를 누르면 프로그램 종료
        break
    # 마우스 왼쪽 버튼을 떼고 Shift 키가 눌리지 않은 상태에서 다각형 그리기
    elif not shift_down and len(polyPt) > 2:
        cv2.polylines(img, [np.array(polyPt, np.int32)], isClosed=True, color=(255, 0, 0), thickness=1)
        polyPt.clear()  # 다각형을 그린 후 리스트 초기화
cv2.destroyAllWindows()

cv2.imwrite('mission_img.png', img)

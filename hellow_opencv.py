
import sys
import cv2

# opencv 버전 확인
print('Hello OpenCV', cv2.__version__)

# image read('파일명')
# img의 데이터타입 numpy.ndarray
img_gray = cv2.imread("data/hanni.jpg", cv2.IMREAD_GRAYSCALE)
img_bgr = cv2.imread("data/hanni.jpg")

# 파일을 못 찾아서 이미지를 못 읽어온 경우
# 프로그램 종료
# 어디서 예외가 났는지 알기 편하게 예외처리 루틴으로 추가하자!
if img_gray is None or img_bgr is None:
    print('Image load failed!')
    sys.exit()

cv2.imshow('image_gray', img_gray)  # 이미지를 창에 띄워준다, 'image'창에 읽어온 img 배열을 출력
cv2.imshow('image_bgr', img_bgr)
cv2.waitKey()             # 키 입력을 기다리는 함수, 함수 안 값의 입력 단위 : ms, 인수값(딜레이값)을 설정하지 않으면 키보드 입력이 주어지기 전까지 무한 대기
cv2.destroyAllWindows()   # 모든 창을 다 닫는다.
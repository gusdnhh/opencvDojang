# 이미지 불러오기 : 동일
# opencv 패키지의 특성과 matplotlib 패키지의 특성의 차이를 이해
# 이미지 출력하기 : cv2.imshow() --> plt.imshow()

import cv2
import sys
import matplotlib.pyplot as plt

fileName = 'data/data/cat.jpg'

img_bgr = cv2.imread(fileName) # 이미 bgr 순서로 불러온 상태

if img_bgr is None:
    sys.exit("Image load is failed")
    
# opencv 모듈은 이미지를 읽어올떄 색상 공간의 순서를 b,g,r 로
# matplotlib 모듈은 이미지를 읽어올떄 색상 공간의 순서를 r,g,b 로

# 컬러 스페이스(채널순서)를 바꿔주는 함수
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.axis('off') # matplotlib의 imshow에서 눈금을 표시하지 x
plt.show()

cv2.imshow('img2',img_bgr)

cv2.waitKey()
cv2.destroyAllWindows()
# 파일에서 이미지를 읽어서 출력

import cv2
import sys

fileName = "data/data/cat.jpg"

img = cv2.imread(fileName)
print(img.shape)

# 예외처리 루틴
if img is None:
    print("Image load fall")
    # 프로그램 종료
    sys.exit()

# 창에 이미지를 출력
# 창의 이름을 img
cv2.namedWindow('img', cv2.WINDOW_FULLSCREEN)
cv2.imshow('img',img)

# 'q'키를 눌렀을 때 창이 종료되게

# 이미지 배열을 파일로 저장하는 함수
cv2.imwrite('cat1.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 0])
cv2.imwrite('cat2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 80])


loop = True
while loop:
    inKey = cv2.waitKey()
    print(inKey)
    if inKey == ord('q'):
        # 'img'창 닫기
        cv2.destroyWindow('img')
        loop = False
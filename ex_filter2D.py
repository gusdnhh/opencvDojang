import cv2
import numpy as np

src = cv2.imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

# 사용자 커널(=필터)를 생성해서
kernel = np.ones((3,3), dtype = np.float32)/9
dst = cv2.filter2D(src,-1,kernel)

# blur 커널을 사용해서
dst2 = cv2.blur(src, (3,3))

# embosing 커널 생성
mask1 = np.array([[-2,-1,0],[-1,1,1],[0,1,2]])
dst3 = cv2.filter2D(src, -1, mask1)

cv2.imshow('img', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.waitKey()
cv2.destroyAllWindows()
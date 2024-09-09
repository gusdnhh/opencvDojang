import cv2,sys
import numpy as np

src = cv2.imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image load failed')

# blur처리
# 필터의 크기가 (3x3)

ksize = 1
kernel = (ksize,ksize)
dst = cv2.blur(src, kernel)
dst2 = cv2.blur(src, (10,10))

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)

cv2.waitKey()
cv2.destroyAllWindows()
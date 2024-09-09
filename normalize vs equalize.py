import cv2, sys
import numpy as np
import matplotlib.pyplot as plt

# grayscale로 읽어오기
src = cv2.imread('data2/Hawkes.jpg',cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('image load failed')


dst1 = cv2.equalizeHist(src)
dst2 = cv2.normalize(src,None, 0, 255, cv2.NORM_MINMAX)

hist = cv2.calcHist([src],[0],None, [256],[0,256])
hist1 = cv2.calcHist([dst1],[0],None, [256],[0,256])
hist2 = cv2.calcHist([dst2],[0],None, [256],[0,256])

cv2.imshow('img',src)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)

plt.plot(hist)
plt.plot(hist1)
plt.plot(hist2)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
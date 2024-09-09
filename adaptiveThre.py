import cv2
from mylib import hist_gray 

src = cv2.imread(r'data\srcThreshold.png', cv2.IMREAD_GRAYSCALE)


dst = cv2.adaptiveThreshold(src,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 7)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()
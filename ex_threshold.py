import cv2
from mylib import hist_gray 

src = cv2.imread(r'data2\srcThreshold.png', cv2.IMREAD_GRAYSCALE)

hist_gray(src)
_, src_th = cv2.threshold(src, 200, 255, cv2.THRESH_BINARY)

cv2.imshow('thre',src_th)
cv2.waitKey()
cv2.destroyAllWindows()
import cv2, sys
import numpy as np
import matplotlib.pyplot as plt

isColor = True

if not isColor:
    src1 = cv2.imread('data2/Hawkes.jpg')
    src2 = cv2.imread('data2/Hawkes_norm.jpg')

    if src1 is None:
        sys.exit("Image load failed!")

    # 히스토그램을 만들기
    hist1 = cv2.calcHist([src1], [3], None, [256,256,256], [0,256])
    hist2 = cv2.calcHist([src2], [3], None, [256,256,256], [0,256])


if isColor:
    src = cv2.imread('data/lena.bmp')
    
    
    if src is None:
        sys.exit("image load failed!")
        
    # 컬러 채널 분리
    src[:,:,2] = np.clip(src[:,:,2] - 100, 0, 255)
    colors = ['b','g','r']
    bgr_planes = cv2.split(src)
    
    for (p,c) in zip(bgr_planes, colors):
        hist = cv2.calcHist([p],[0],None,[256],[0,256])
        plt.plot(hist, color=c)
    
    
# cv2.imshow('src', src)

cv2.imshow('img',src)
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
import cv2
import numpy as np
import matplotlib.pyplot as plt

isColor = False




if not isColor:
    
    # grayscale 
    src = cv2.imread('data2/candies.png',cv2.IMREAD_GRAYSCALE)
    
    dst1 = cv2.add(src,50)
    hist1 = cv2.calcHist([src], [0], None, [256], [0,256])
    hist2 = cv2.calcHist([dst1], [0], None, [256], [0,256])



if isColor:
    dst1 = cv2.add(src,(100,100,100))


# 밝기 변환
# dst1 = cv2.add(src,100)
# dst2 = src + 100

# # 범위를 0~255로 지정하고 덧셈연산을 수행
# dst3 = np.clip(src + 100,0,255)
plt.plot(hist1)
plt.plot(hist2)
plt.show()
cv2.imshow('src',src)
cv2.imshow('dst1',dst1)
cv2.waitKey()
cv2.destroyAllWindows()
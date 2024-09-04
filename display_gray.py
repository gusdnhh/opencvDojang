# plt.imshow함수에서 imterpolation 옵션
# cmap은 이미지가 컬러일 경우 cmap지정을 안해도 컬러로 출력
# cmap = 'gray'

import cv2
import sys
import matplotlib.pyplot as plt

fileName = 'data/data/cat.jpg'

imgGray = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)
print(imgGray.shape)

plt.axis('off')
plt.imshow(imgGray, cmap ='gray', interpolation = 'bicubic')
plt.show()
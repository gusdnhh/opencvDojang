# 건물의 윤곽선을 뚜렷하게 처리한 다음, 너무 밝은 부분만 선택해 밝기를 줄임


import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread(r'mission\03.png')



# Kernel for unsharp mask (sharpening)
kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])

dst1 = cv2.filter2D(image, -1, kernel)

# Convert the image from BGR to HSV
hsv = cv2.cvtColor(dst1, cv2.COLOR_BGR2HSV)

# Split the HSV channels
h, s, v = cv2.split(hsv)

# Define a threshold for bright areas (this can be adjusted as needed)
threshold_value = 180

# Reduce the brightness of pixels with a value higher than the threshold
v[v > threshold_value] -= 50  # Reduce the brightness by 50 (adjust as needed)

# Merge the channels back together
hsv_modified = cv2.merge([h, s, v])

# Convert the image back to BGR
dst2 = cv2.cvtColor(hsv_modified, cv2.COLOR_HSV2BGR)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
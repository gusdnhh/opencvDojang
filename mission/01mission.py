# 밤하늘의 노이즈를 제거하고, 건물의 윤곽선을 다시 살림

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread(r'mission\01.png')

# Apply Fast Non-Local Means Denoising for color images
dst1 = cv2.fastNlMeansDenoisingColored(image, None, 20, 20, 7, 21)

# Kernel for unsharp mask (sharpening)
kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])

# Apply the sharpening filter to the denoised image
dst2 = cv2.filter2D(dst1, -1, kernel)

cv2.imshow('dst2',dst2)
cv2.waitKey()
cv2.destroyAllWindows()
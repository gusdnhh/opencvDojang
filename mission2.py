import cv2
import numpy as np


def scale(src, x_scale, y_scale):
    h, w = src.shape[:2]
    aff = np.array([[x_scale, 0, 0],[0, y_scale, 0]], dtype = np.float32)
    dst = cv2.warpAffine(src, aff, (int(w*x_scale),int(h*y_scale)))
    return dst

src = cv2.imread('mission_img.png')


none_blur = scale(src, 0.5, 0.5)

src_blur = cv2.blur(src,(3,3))

yes_blur = scale(src_blur, 0.5, 0.5)

merged = np.hstack((none_blur,yes_blur))

cv2.imshow('blur vs oasis', merged)
cv2.waitKey()
cv2.destroyAllWindows()
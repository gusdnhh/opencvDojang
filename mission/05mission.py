
import cv2
import numpy as np
from matplotlib import pyplot as plt

src = cv2.imread(r'mission\05.png')

dst1 = cv2.normalize(src, None, 0, 200, cv2.NORM_MINMAX)

cv2.imshow('dst1',dst1)
cv2.waitKey()
cv2.destroyAllWindows()
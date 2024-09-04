
# 이미지 4장을 불러온다
# 이미지 4장을 하나의 차에 띄운다.

import cv2, sys
import matplotlib.pyplot as plt

imgBRG1= cv2.imread('data/data/lena.jpg')
imgBRG2= cv2.imread('data/data/orange.jpg')
imgBRG3= cv2.imread('data/data/apple.jpg')
imgBRG4= cv2.imread('data/data/baboon.jpg')

if imgBRG1 is None or imgBRG2 is None or imgBRG3 is None or imgBRG4 is None:
    sys.exit('Image load is failed')
    
imgRGB1 = cv2.cvtColor(imgBRG1, cv2.COLOR_BGR2RGB)
imgRGB2 = cv2.cvtColor(imgBRG2, cv2.COLOR_BGR2RGB)
imgRGB3 = cv2.cvtColor(imgBRG3, cv2.COLOR_BGR2RGB)
imgRGB4 = cv2.cvtColor(imgBRG4, cv2.COLOR_BGR2RGB)

# plt.subplots로 이미지를 출력
figsize = (10,10)
fig, ax = plt.subplots(2,2, figsize = figsize)

ax[0][0].axis('off')
ax[0][1].axis('off')
ax[1][0].axis('off')
ax[1][1].axis('off')

ax[0][0].imshow(imgRGB1, aspect='auto')
ax[0][1].imshow(imgRGB3, aspect='auto')
ax[1][0].imshow(imgRGB4, aspect='auto')
ax[1][1].imshow(imgRGB2, aspect='auto')

fig.canvas.manager.set_window_title("Sample windows")
fig.suptitle('Sample Windows', fontsize=16)

plt.show()
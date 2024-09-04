import cv2
import numpy as np

# 이미지 불러오기
img = cv2.imread('data2/opencv-logo-white.png', cv2.IMREAD_UNCHANGED)
if img is None:
    print("이미지를 불러오지 못했습니다. 경로를 확인하세요.")
    sys.exit()

# 모든 행, 열, 0~2번 채널 (BGR 채널만 추출)
src = img[:,:,0:3].copy()

# 알파 채널만 슬라이싱
mask = img[:,:,3].copy()

# 목적지 이미지 불러오기
dst = cv2.imread('data2/cat.bmp')
if dst is None:
    print("목적지 이미지를 불러오지 못했습니다. 경로를 확인하세요.")
    sys.exit()

# dst의 크기에 맞게 src와 mask를 리사이즈
src_resized = cv2.resize(src, (dst.shape[1], dst.shape[0]))
mask_resized = cv2.resize(mask, (dst.shape[1], dst.shape[0]))

# 마스크 연산을 통해 src_resized를 dst에 덮어씌우기
cv2.copyTo(src_resized, mask_resized, dst)

# 결과 이미지 표시
cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

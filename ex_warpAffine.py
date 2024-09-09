import cv2, sys
import numpy as np
import math
0
def translate(src, x_move, y_move):    
    # 이미지의 이동 변환 x-> 200, y->100만큼 이동
    # 이동변환 행렬 생성
    h, w = src.shape[:2]
    aff = np.array([[1, 0, x_move],[0, 1, y_move]], dtype = np.float32)
    # 변환후에 출력되는 배열의 크기 (입력되는 배열의 크기 그래도 출력)
    dst = cv2.warpAffine(src, aff, (w + x_move, h + y_move))
    return dst

def shear(src, x_shear=0, y_shear=0):
    h, w = src.shape[:2]
    if x_shear>0 and y_shear==0:
        aff = np.array([[1, x_shear,0],[0,1,0]],dtype=np.float32)
        dst = cv2.warpAffine(src,aff, (w+ int(h*x_shear), h))
    elif y_shear > 0 and x_shear==0:
        aff = np.array([[1, 0,0],[0,y_shear,0]],dtype=np.float32)
        dst = cv2.warpAffine(src,aff, (w, h + int(w*y_shear)))
        
    return dst

def scale(src, x_scale, y_scale):
    h, w = src.shape[:2]
    aff = np.array([[x_scale, 0, 0],[0, y_scale, 0]], dtype = np.float32)
    dst = cv2.warpAffine(src, aff, (int(w*x_scale),int(h*y_scale)))
    return dst

def rotate(src, rad):
    aff = np.array([[np.cos(rad), np.sin(rad), 0],
                    [-np.sin(rad), np.cos(rad), 0]], dtype=np.float32)
    dst = cv2.warpAffine(src,aff,(0,0))
    return dst

def rotate2(src,angle):
    h,w = src.shape[:2]
    # 튜플로 centerPt를 저장
    centerPt = (w//2,h//2)
    # getRotationMatrix2D가 변환행렬을 만들어줌
    rot = cv2.getRotationMatrix2D(centerPt, angle, 1)
    dst = cv2.warpAffine(src, rot, (w,h))
    return dst


src = cv2.imread(r'data2\kids1.png')

if src is None:
    sys.exit('Image load failed')

dst1 = cv2.resize(src, (0,0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
dst2 = cv2.resize(src, (0,0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
dst3 = cv2.resize(src, (0,0), fx=4, fy=4, interpolation=cv2.INTER_LANCZOS4)
    
# dst1 = translate(src, 100, 50)
# dst2 = shear(src, 0.5, 0)
# dst3 = scale(src, 2, 2)

# cv2.imshow('src', src)
# cv2.imshow('INTER_CUBIC', dst1)
# cv2.imshow('INTER_NEAREST', dst2)
# cv2.imshow('INTER_LANCZOS4', dst3)

angle = 20
rad = angle*math.pi/180
dst4 = rotate(src, rad)
dst5 = rotate2(src, angle)

cv2.imshow('rotate',dst4)
cv2.imshow('rotate_centerPt',dst5)
cv2.waitKey()
cv2.destroyAllWindows()
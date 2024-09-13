import cv2, sys
import os
import shutil




classlist = ['airPod', 'whitePen', 'blackPen', 'CarKey']

def createFolder():
    
    
    for classname in classlist:
        # 기존에 폴더가 있으면 삭제하고, 새로 생성
        # 폴더 안에 파일이 존재하더라도, 파일과 폴더를 모두 삭제
        if
        
        shutil.rmtree()
        os.makedirs(os.path.join(dataOrg, classname),exist_ok=True)


def resize(img=None, dsize = dsize, imgName=None):
    if img is None:
        print("image Path is None")
        
    dst = cv2.resize(img, dsize=dsize, )
import cv2
import numpy as np
from glob import glob
import os

# 0. 파일 목록 읽기(data폴더) *.jpg -> 리스트
# 1. 이미지 불러오기
# 2. 마우스 콜백함수 생성
# 3. 콜백함수 안에서 박스를 그리고 박스 좌표를 뽑아낸다.(마우스 좌표 2개)
#    참고로 YOLO에서는 박스의 중심좌표(x,y), w,h
# 4. 이미지 파일명과 동일한 파일명으로(확장자만 때고) txt파일 생성
# 추가 기능 0 : 박스를 잘못 쳤을 때 'c'를 누르면 현재파일의 박스 내용 초기화
# 추가 기능 : 화살표(->)를 누르면 다음 이미지 로딩되고 (1~4 반복)
# 추가 기능 : 화살표(<-)를 눌렀을 때 txt 파일이 있다면 박스를 이미지 위에 띄워주기


# 파일 목록 가져오기 함수
def getImageList(filename):
    # 현재 작업 디렉토리 확인
    basePath = os.getcwd()
    dataPath = os.path.join(basePath, filename)
    fileNames = glob(dataPath + '/*.jpg')
    return fileNames

# 박스를 그리기 위한 함수
def drawROI(img, boxes):
    cpy = img.copy()
    line_c = (128,128,255)
    linewidth = 2
    
    # 여러 개의 박스를 그리기 위해 반복문 사용
    for box in boxes:
        cv2.rectangle(cpy, box[0], box[1], color=line_c, thickness=linewidth)
    
    return cpy

# 마우스 콜백함수
def onMouse(event, x, y, flags, param):
    global img, current_box, all_boxes, box_dict, current_index, fileNames
    cpy = img.copy()
    
    if event == cv2.EVENT_LBUTTONDOWN:
        current_box = [(x, y)] # 시작점 저장
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if len(current_box) == 1: # 마우스 드래그 중일 떄
            temp_img = drawROI(cpy, all_boxes) # 기존 박스를 먼저 그림
            cv2.rectangle(temp_img, current_box[0], (x,y), (128,128,255), 2) # 현재 드래그 중인 박스 표시
            cv2.imshow('label', temp_img)
    
    elif event == cv2.EVENT_LBUTTONUP:
        if len(current_box) == 1: # 마우스를 떼면 끝점 저장
            current_box.append((x,y)) # 끝점 좌표 추가
            all_boxes.append(current_box) # 전체 박스 리스트에 추가
            box_dict[fileNames[current_index]] = all_boxes.copy() # 해당 이미지의 박스를 저장
            current_box = [] # 박스 초기화
            cpy = drawROI(img, all_boxes) # 모든 박스를 그림
            cv2.imshow('label', cpy)

# 박스 좌표 리스트 초기화
box_dict = {} # 각 이미지에 대한 박스 정보 저장
all_boxes = [] # 현재 이미지의 박스 리스트
current_box = [] # 드래그 중인 박스

# 이미지 파일 목록 가져오기        
fileNames = getImageList('images')
print(fileNames)
current_index = 0 # 초기 이미지 인덱스

# 첫 번째 이미지 불러오기
img = cv2.imread(fileNames[current_index])

cv2.namedWindow('label')
cv2.setMouseCallback('label', onMouse)
cv2.imshow('label', img)

while True:
    key = cv2.waitKey(0)
    
    if key == 27:
        break
    
    
    elif key == ord('s'):
        filename, ext = os.path.splitext(fileNames[current_index])
        textfilename = filename + '.txt'
        with open(textfilename, 'w') as file:
            for box in all_boxes:
                file.write(f"{box[0][0]},{box[0][1]},{box[1][0]},{box[1][1]}\n")
        print(f"파일이 성공적으로 저장되었습니다.")
    
    elif key == ord('c'):
        img = cv2.imread(fileNames[current_index])
        cv2.imshow('label', img)
        all_boxes = []
        current_box = []
        if fileNames[current_index] in box_dict:
            del box_dict[fileNames[current_index]]
        
        filename, ext = os.path.splitext(fileNames[current_index])
        textfilename = filename + '.txt'
        
        if os.path.exists(textfilename):
            os.remove(textfilename)
    
    # 'a' 키를 눌러 이전 파일로
    elif key == ord('a'):
        if current_index > 0:
            current_index -= 1
            img = cv2.imread(fileNames[current_index])
            if fileNames[current_index] in box_dict:
                all_boxes = box_dict[fileNames[current_index]]
            else:
                all_boxes = []
            img = drawROI(img, all_boxes)
            cv2.imshow('label', img)
        else:
            print('이전 이미지가 없습니다.')
    
    # 'd' 키를 눌러 다음 파일로
    elif key == ord('d'):
        if current_index < len(fileNames) - 1:
            current_index += 1
            img = cv2.imread(fileNames[current_index])
            if fileNames[current_index] in box_dict:
                all_boxes = box_dict[fileNames[current_index]]
            else:
                all_boxes = []
            img = drawROI(img, all_boxes)
            cv2.imshow('label', img)
        else:
            print('다음 이미지가 없습니다.')        

cv2.destroyAllWindows()
     

import cv2
import os
from glob import glob

# 이미지 파일 목록 읽기(data 폴더 내 *.jpg)
def getImageList(foldername):
    basePath = os.getcwd()
    dataPath = os.path.join(basePath, foldername)
    fileNames = glob(dataPath + '/*.jpg')
    return fileNames

# ROI 좌표를 텍스트 파일로 저장하는 함수
def saveROIToFile(file_path, x, y, w, h, key):
    global img
    fh, fw = img.shape[:2]
    with open(file_path, 'w') as file:
        cx = x + w / 2
        cy = y + h / 2
        pw = int(w/fw)
        ph = int(h/fh)
        file.write(f"{cx},{cy},{pw},{ph}\n")
        file.write(f"Key pressed: {key}\n")
    print(f"파일이 성공적으로 저장되었습니다: {file_path}")

# 메인 로직
def processImages():
    # 파일 리스트를 얻어오기
    fileNames = getImageList('images')

    cat_count = 1
    person_count = 1
    current_index = 0  # 현재 이미지 인덱스

    while True:
        img = cv2.imread(fileNames[current_index])
        if img is None:
            print(f"이미지 로드 실패: {fileNames[current_index]}")
            break

        # ROI 선택
        x, y, w, h = cv2.selectROI('img', img, False)

        key = cv2.waitKey(0)
        
        # '0'을 누르면 고양이, '1'을 누르면 사람 파일로 저장
        if key == ord('0'):
            file_path = f"{os.getcwd()}/images_txt/cat{cat_count}.txt"
            saveROIToFile(file_path, x, y, w, h, key)
            cat_count += 1
        elif key == ord('1'):
            file_path = f"{os.getcwd()}/images_txt/person{person_count}.txt"
            saveROIToFile(file_path, x, y, w, h, key)
            person_count += 1
        
        up = cv2.waitKey(0)

        # 오른쪽 화살표: 다음 이미지
        if key == 224:  # 특수 키 감지 (윈도우에서는 224, 리눅스/맥에서는 0)
            key = cv2.waitKey(0)
            if key == 83:  # 오른쪽 화살표
                current_index = (current_index + 1) % len(fileNames)  # 인덱스 순환
            elif key == 81:  # 왼쪽 화살표
                current_index = (current_index - 1) % len(fileNames)  # 인덱스 순환

        
        # ESC 키를 누르면 종료
        elif key == 27:
            break

    cv2.destroyAllWindows()

# 프로그램 실행
processImages()

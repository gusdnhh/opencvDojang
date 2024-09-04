import os
import cv2
import time
from datetime import datetime
import shutil
import sys

def get_folder_size(folder_path):
    """폴더의 전체 크기를 바이트 단위로 계산"""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if not os.path.islink(file_path):  # 심볼릭 링크는 제외
                total_size += os.path.getsize(file_path)
    return total_size

def delete_oldest_folder(base_path):
    """폴더 경로 내에서 가장 오래된 폴더를 삭제"""
    folders = [os.path.join(base_path, folder) for folder in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, folder))]
    if not folders:
        return
    
    # 폴더 생성 시간으로 정렬 (가장 오래된 것이 첫 번째)
    oldest_folder = min(folders, key=os.path.getctime)
    
    # 폴더 삭제
    shutil.rmtree(oldest_folder)
    print(f"가장 오래된 폴더 삭제됨: {oldest_folder}")

def manage_folder_size(base_path, max_size_gb):
    """폴더 용량이 max_size_gb를 넘으면 가장 오래된 폴더를 삭제"""
    max_size_bytes = max_size_gb * 1024 * 1024 * 1024  # GB -> Bytes
    current_size = get_folder_size(base_path)
    
    while current_size > max_size_bytes:
        delete_oldest_folder(base_path)
        current_size = get_folder_size(base_path)
        
# 기본 경로 및 최대 용량 설정
base_path = "blackboxfile"
max_size_gb = 0.5  # 최대 용량 500MB

# 카메라에서 클래스 객체 생성
cap = cv2.VideoCapture(r'data\video.mp4')

if not cap.isOpened():
    sys.exit()

# 카메라로 담는 영상의 기본 정보
frameSize = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'XVID')

while True:
    # 현재 시각을 가져와 파일명과 폴더명 만들기
    now = datetime.now()
    folder_name = now.strftime("%Y-%m-%d_%H")
    file_name = now.strftime("%Y-%m-%d %H-%M-%S")
    full_folder_path = os.path.join(base_path, folder_name)

    # 폴더가 존재하지 않으면 생성
    if not os.path.exists(full_folder_path):
        os.makedirs(full_folder_path)

    # 비디오 파일 경로 설정 및 VideoWriter 객체 생성
    out = cv2.VideoWriter(os.path.join(full_folder_path, f'{file_name}.mp4'), fourcc, fps, frameSize)

    print(f"비디오 파일이 {full_folder_path} 경로에 저장됩니다: {file_name}.mp4")

    start_time = time.time()

    while True:
        # 한 프레임 영상 읽어오기
        retval, frame = cap.read()
        
        # 카메라에서부터 영상이 정상적으로 전달되었는지 확인
        if not retval:
            break
        
        # 동영상 녹화기에 프레임 전달
        out.write(frame)
        
        # 현재 시간을 측정하여 파일을 1분 단위로 자름
        elapsed_time = time.time() - start_time
        if elapsed_time >= 60:  # 60초가 경과했으면 루프 종료
            break
        
        # 영상 표시 (옵션)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    out.release()

    # 폴더 용량 관리 (파일이 끝날 때마다 한 번만 실행)
    manage_folder_size(base_path, max_size_gb)

cap.release()
cv2.destroyAllWindows()
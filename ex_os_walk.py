import os

def list_files_and_dirs(directory):
    # os.walk() 함수를 사용하여 디렉토리와 파일을 순회
    for dirpath, dirnames, filenames in os.walk(directory):
        print(f"현재 디렉토리: {dirpath}")
        
        # 현재 디렉토리의 하위 디렉토리를 출력
        for dirname in dirnames:
            print(f"  디렉토리: {os.path.join(dirpath, dirname)}")
        
        # 현재 디렉토리의 파일들을 출력
        for filename in filenames:
            print(f"  파일: {os.path.join(dirpath, filename)}")
        
        print()  # 한 디렉토리의 내용을 출력한 후 줄바꿈

# 예제 사용
directory_path = r"C:\Users\SBA\opencvDojang\ex1"  # 탐색하고자 하는 디렉토리 경로를 입력
list_files_and_dirs(directory_path)

print(os.path.getsize(r"C:\Users\SBA\opencvDojang\data\1.png"))
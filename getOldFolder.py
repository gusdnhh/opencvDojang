import os
from datetime import datetime

# 폴더를 생성
# 현재 폴더 아래에 test 폴더를 생성
# test폴더 아래에 날짜_시간 폴더를 생성

basePath = 'test'

# 폴더를 만드는 함수
os.makedirs(basePath, exist_ok=True)

now = datetime.now()
# 폴더명을 "20240904_11"

# folderName = now.strftime("%Y%m%d_%H")
for hour in range(24):
    folderName = now.strftime("%Y%m%d_")
    folderName = folderName + str(hour)
    folderName = os.path.join(basePath, folderName)
    os.makedirs(folderName, exist_ok=True)

os.makedirs('test/20240904_0', exist_ok=True)

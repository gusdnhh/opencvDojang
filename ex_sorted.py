import os
from datetime import datetime

folderName = os.listdir('test')

# 리스트를 오래된 순으로 정렬
sorted_list = sorted(folderName, key=lambda date: datetime.strptime(date, "%Y%m%d_%H"))

# 결과 출력
print("오래된 순으로 정렬된 리스트:")
for date in sorted_list:
    print(date)

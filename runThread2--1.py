import threading
import time

# 스레드에서 계산한 부분 합을 저장할 변수
partial_sum1 = 0
partial_sum2 = 0

def partial_sum(start, end, result_holder, index):
    """주어진 범위의 합을 계산하고, 결과를 result_holder 리스트에 저장"""
    result_holder[index] = sum(range(start, end + 1))

# 시작 시간 기록
start_time = time.time()

# 두 스레드의 결과를 저장할 리스트
results = [0, 0]

# 두 개의 스레드 생성
thread1 = threading.Thread(target=partial_sum, args=(1, 50000000, results, 0))
thread2 = threading.Thread(target=partial_sum, args=(50000001, 100000000, results, 1))

# 스레드 시작
thread1.start()
thread2.start()

# 스레드가 끝날 때까지 대기
thread1.join()
thread2.join()

# 두 스레드의 결과를 합침
total_sum = results[0] + results[1]

# 종료 시간 기록
end_time = time.time()

# 실행 시간 계산
execution_time = end_time - start_time

# 결과 출력
print(f"1부터 100,000,000까지의 합: {total_sum}")
print(f"실행 시간: {execution_time:.4f}초")

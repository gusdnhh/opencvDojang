import threading
import time

# 결과를 저장할 전역 변수
total_sum = 0

# 락 객체 생성 (스레드 간 데이터 동기화)
lock = threading.Lock()

# 스레드에서 실행할 함수 정의
def partial_sum(start, end):
    global total_sum
    part_sum = sum(range(start, end + 1))
    
    # 락을 사용하여 total_sum에 안전하게 더하기
    with lock:
        total_sum += part_sum

# 시작 시간 기록
start_time = time.time()

# 두 개의 스레드 생성
thread1 = threading.Thread(target=partial_sum, args=(1, 50000000))
thread2 = threading.Thread(target=partial_sum, args=(50000001, 100000000))

# 스레드 시작
thread1.start()
thread2.start()

# 스레드가 끝날 때까지 대기
thread1.join()
thread2.join()

# 종료 시간 기록
end_time = time.time()

# 실행 시간 계산
execution_time = end_time - start_time

# 결과 출력
print(f"1부터 100,000,000까지의 합: {total_sum}")
print(f"실행 시간: {execution_time:.4f}초")

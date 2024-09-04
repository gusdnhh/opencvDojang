import time

# 시작 시간 기록
start_time = time.time()

# 1부터 100,000,000까지의 합 계산
total_sum = sum(range(1, 100000001))

# 종료 시간 기록
end_time = time.time()

# 실행 시간 계산
execution_time = end_time - start_time

# 결과 출력
print(f"1부터 100,000,000까지의 합: {total_sum}")
print(f"실행 시간: {execution_time:.4f}초")

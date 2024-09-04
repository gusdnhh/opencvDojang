import multiprocessing
import time

def partial_sum(start, end, result_queue):
    """주어진 범위의 합을 계산하고 결과를 큐에 저장"""
    result_queue.put(sum(range(start, end + 1)))

if __name__ == "__main__":
    # 시작 시간 기록
    start_time = time.time()

    # 결과를 저장할 큐 생성
    result_queue = multiprocessing.Queue()

    # 프로세스 당 처리할 범위 계산
    total_numbers = 100000000
    range_per_process = total_numbers // 2

    # 프로세스 생성
    processes = []
    for i in range(2):
        start = i * range_per_process + 1
        end = (i + 1) * range_per_process if i != 1 else total_numbers
        process = multiprocessing.Process(target=partial_sum, args=(start, end, result_queue))
        processes.append(process)

    # 프로세스 시작
    for process in processes:
        process.start()

    # 프로세스 종료 대기
    for process in processes:
        process.join()

    # 큐에서 결과를 가져와 합산
    total_sum = 0
    while not result_queue.empty():
        total_sum += result_queue.get()

    # 종료 시간 기록
    end_time = time.time()

    # 실행 시간 계산
    execution_time = end_time - start_time

    # 결과 출력
    print(f"1부터 100,000,000까지의 합: {total_sum}")
    print(f"실행 시간: {execution_time:.4f}초")

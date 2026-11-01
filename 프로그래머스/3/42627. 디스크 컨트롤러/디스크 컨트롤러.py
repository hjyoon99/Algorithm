import heapq

def solution(jobs):
    #jobs = [작업 요청 시점, 소요시간]
    # result = 평균 반환 시간 (sum(소요시간) // len(jobs))
    # 파이썬 튜플은 첫 번째 원소를 기준으로 힙이 정렬
    jobs.sort(key=lambda x: x[0]) # 요청시간 빠른 순서로 정렬
    time = 0 # 현재 시간
    i = 0  # jobs 배열 인덱스
    total_time = 0 
    heap = []
    count = 0 # 처리한 작업 수 
    n = len(jobs)
    # 작업 요청 시점 기준 가장 빨리 끝나는 친구 -> heap
    
    while count < n:
        # 현재 시간(time)까지 요청된 작업들을 모두 힙에 넣기
        while i < n and jobs[i][0] <= time:
            # [소요 시간, 요청 시점]
            heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
            i += 1
        # 힙에 대기 중인 작업이 있다면 가장 소요 시간이 짧은 것 처리
        if heap:
            duration, start = heapq.heappop(heap)
            time += duration
            total_time += (time - start)
            count += 1
            
        else:
            # 힙이 비어있다면 (현재 시간에 대기 중인 작업이 없음)
            # 하드디스크가 놀고 있으므로, 다음 작업이 요청되는 시점으로 time을 점프시킴
            time = jobs[i][0]
    return total_time // n
    
    
import heapq

def solution(jobs):
    #jobs = [작업 요청 시점, 소요시간]
    # 우선순위 : 작업의 소요시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것
    jobs.sort(key=lambda x: x[0])
    time = 0 # 현재시간
    i = 0
    total_time = 0
    heap = []
    count = 0
    n = len(jobs)
    
    while count < n:
        # 힙에서 요청시점이 현재시간보다 작을 경우
        while i < n and jobs[i][0] <= time:
            # [소요 시간, 요청 시점]
            heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
            i += 1
        # 힙이 있으면 가장 소요시간 짧은애부터
        if heap:
            duration, start = heapq.heappop(heap)
            time += duration
            total_time += (time-start)
            count += 1
        else:
            # 힙이 비어있으면
            # 하드디스크 놀고 있으니까 time 점프
            time = jobs[i][0]
    return total_time//n
    
def solution(distance, rocks, n):
    positions = sorted(rocks) + [distance]
    
    left = 1
    right = distance
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        removed = 0
        prev = 0 # 마지막으로 남긴 위치
        
        for pos in positions:
            if pos - prev < mid:
                removed += 1
            else:
                prev = pos
        if removed <= n:
            answer = mid
            left = mid + 1 # 더 큰 간격도 가능한지 확인
            
        else:
            right = mid - 1 # 제거할 바위 너무 많음
    return answer
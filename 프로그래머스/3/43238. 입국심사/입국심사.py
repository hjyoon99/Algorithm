def solution(n, times):
    left = 1
    right = min(times) * n
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        # mid 분 동안 처리 가능한 최대 인원
        count = 0
        for t in times:
            count += mid // t
            
        if count >= n:
            answer = mid
            right = mid -1
        else:
            left = mid + 1
    return answer
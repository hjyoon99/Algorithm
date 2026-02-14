def solution(n):
    count = 0
    start = 1
    end = 1
    total = 1
    
    while start <= n:
        if total == n:
            count += 1
            total -= start
            start += 1
        elif total < n:
            end += 1
            total += end
        else:
            total -= start
            start += 1
    return count
        
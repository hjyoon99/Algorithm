def solution(k, m, score):
    earned = 0
    
    score.sort(reverse = True)
    result = [score[i:i + m] for i in range(0, len(score), m)]

    
    for arr in result:
        if len(arr) == m:
            arr.sort()
            earned += arr[0] * m
    
    return earned
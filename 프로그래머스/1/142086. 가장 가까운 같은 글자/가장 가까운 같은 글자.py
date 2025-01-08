def solution(s):
    prev_idx = {}
    result = []
    
    for i, value in enumerate(s):
        if value not in prev_idx:
            result.append(-1)
        else:
            result.append(i-prev_idx[value])
        prev_idx[value] = i
        
        
    return result
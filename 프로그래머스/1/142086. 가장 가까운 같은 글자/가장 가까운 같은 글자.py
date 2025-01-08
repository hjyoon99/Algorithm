def solution(s):
    prev_idx = {}
    tmp = []
    result = []
    
    for i, value in enumerate(s):
        if value not in tmp:
            tmp.append(value)
            result.append(-1)
            prev_idx[value] = i
        else:
            tmp.append(value)
            result.append(i-prev_idx[value])
            prev_idx[value] = i
        
        
    return result
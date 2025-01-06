def solution(t, p):
    result = 0
    
    for i in range(0, len(t)-len(p)+1):
        num = int(t[i:i+len(p)])
        if(num <= int(p)):
            result += 1
    
    return result
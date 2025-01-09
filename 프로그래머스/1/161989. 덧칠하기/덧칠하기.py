import math

def solution(n, m, section):
    result = 0
    max_paint = 0
    
    for start in section:
        if start > max_paint:
            result += 1
            max_paint = start + m - 1
    
    return result
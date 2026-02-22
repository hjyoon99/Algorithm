from collections import defaultdict

def solution(clothes):
    answer = 1
    count = defaultdict(int)
    for cloth, kind in clothes:
        count[kind] += 1
    
    for k, v in count.items():
        answer *= (v + 1)
        
    return answer - 1
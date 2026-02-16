from collections import Counter

def solution(k, tangerine):
    # 1. 귤 크기별 개수 세기
    counter = Counter(tangerine)
    
    # 2. 개수를 내림차순 정렬
    counts = sorted(counter.values(), reverse=True)
    
    total = 0
    kinds = 0
    
    # 3. 많은 것부터 담기
    for count in counts:
        total += count
        kinds += 1
        if total >= k:
            break
    
    return kinds

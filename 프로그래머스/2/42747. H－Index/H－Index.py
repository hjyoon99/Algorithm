def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    count = 0
    for i in range(len(citations)):
        h = i + 1
        for cite in citations:
            if cite >= h:
                count += 1
        if count >= h:
            answer = h
        count = 0
        
            
    return answer
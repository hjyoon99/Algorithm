from collections import deque

def solution(prices):
    answer = []
    queue = deque((p, i) for i, p in enumerate(prices))
    index = 1
    
    while queue:
        q = queue.popleft()
        count = 0
        for i in range(q[1] + 1, len(prices)):
            count += 1
            if q[0] > prices[i]:
                break
            
        
        answer.append(count)

    return answer
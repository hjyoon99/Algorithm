from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    queue = deque(progresses)
    day = []
    
    for i in range(len(queue)):
        p = queue.popleft()
        day.append(math.ceil((100 - p) / speeds[i]))
        
    current = day[0]
    count = 1
    
    for i in range(1, len(day)):
        if day[i] <= current:
            count += 1
        else:
            answer.append(count)
            current = day[i]
            count = 1
    answer.append(count)
    return answer
from collections import deque
import math

def solution(progresses, speeds):
    
    days = deque()
    answer = []
    
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    maxd = days[0]
    cnt = 0
    for day in days:
        if day <= maxd:
            cnt += 1
        else:
            answer.append(cnt)
            maxd = day
            cnt = 1
    answer.append(cnt)
              
    return answer
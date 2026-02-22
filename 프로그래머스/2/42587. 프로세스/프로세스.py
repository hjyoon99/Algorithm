from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    for i in range(len(priorities)):
        p = priorities[i]
        queue.append((p, i))
    while queue:
        q = queue.popleft()
        if any(q[0] < other[0] for other in queue):
            queue.append(q)
        else:
            answer += 1
            if q[1] == location:
                return answer
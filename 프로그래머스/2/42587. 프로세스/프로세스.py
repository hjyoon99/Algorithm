from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    while queue:
        q = queue.popleft()
        if any(q[0] < other[0] for other in queue):
            queue.append(q)
        else:
            answer += 1
            if q[1] == location:
                return answer
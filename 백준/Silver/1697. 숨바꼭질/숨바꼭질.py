# 숨바꼭질
from collections import deque

# n > k이면 무조건 n-k초?

n, k = map(int, input().split())

if n > k:
    print(n-k)
else:
    visited = [False]*100001
    q = deque([(n, 0)])

    while q:
        x, time = q.popleft()

        if x == k:
            print(time)
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = True
                q.append((nx, time+1))
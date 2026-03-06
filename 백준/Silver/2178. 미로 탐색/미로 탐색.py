# 미로탐색
from collections import deque

def bfs(x, y):
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if map[nx][ny] == 1:
                    map[nx][ny] = map[x][y] + 1
                    q.append((nx, ny))


n, m = map(int, input().split())

map = [list(map(int, input())) for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs(0, 0)
print(map[n-1][m-1])
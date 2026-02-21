# 2468 안전 영역

import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, num):
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    
    if visited[x][y] or graph[x][y] <= num:
        return

    visited[x][y] = True

    dfs(x-1, y, num)
    dfs(x+1, y, num)
    dfs(x, y-1, num)
    dfs(x, y+1, num)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_height = max(max(row) for row in graph)
answer = 0

for rain in range(max_height + 1):
    visited = [[False]*n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > rain:
                dfs(i, j, rain)
                count += 1

    answer = max(answer, count)

print(answer)
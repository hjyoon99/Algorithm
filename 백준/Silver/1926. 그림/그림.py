# 1926 - 그림
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        count = 1
        count += dfs(x - 1, y)
        count += dfs(x + 1, y)
        count += dfs(x, y + 1)
        count += dfs(x, y - 1)
        return count
    return False

n, m = list(map(int, input().split()))

graph = []
result = 0
max_wid = 0

for i in range(n):
    w = list(map(int, input().split()))
    graph.append(w)

for i in range(n):
    for j in range(m):
        cnt = dfs(i, j)
        max_wid = max(max_wid, cnt)
        if cnt != False:
            result += 1
print(result)
print(max_wid)
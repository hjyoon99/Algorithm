# 음식물 피하기
import sys
sys.setrecursionlimit(100000)
# 가장 큰 덩어리
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    
    
    if graph[x][y] == 1:
        count = 1
        graph[x][y] = 0
        count += dfs(x-1, y)
        count += dfs(x+1, y)
        count += dfs(x, y-1)
        count += dfs(x, y+1)

        return count
    return 0


n, m, k = list(map(int, input().split()))

graph = [[0] * m for _ in range(n)]

for _ in range(k):
    a, b = list(map(int, input().split()))
    graph[a-1][b-1] = 1

result = 0
    
for i in range(n):
    for j in range(m):
        temp = dfs(i, j)
        if temp != 0:
            result = max(result, temp)

print(result)
# 영역 채우기
import sys
sys.setrecursionlimit(10**6)

m, n, k = list(map(int, input().split()))
# (0, 0) - (n, m)

sqr = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = list(map(int, input().split()))

    for i in range(x1, x2):
        for j in range(y1, y2):
            sqr[j][i] = 1

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return 0
    if sqr[x][y] == 0:
        sqr[x][y] = 1
        count = 1
        count += dfs(x-1, y)
        count += dfs(x+1, y)
        count += dfs(x, y-1)
        count += dfs(x, y+1)
        return count
    return 0

result = []
for i in range(n):
    for j in range(m):
        if sqr[j][i] == 0:
            result.append(dfs(j, i))

print(len(result))
result.sort()
print(*result)
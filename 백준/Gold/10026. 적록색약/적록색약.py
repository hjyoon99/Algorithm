# 10026 적록색약
import sys
sys.setrecursionlimit(20000)

def dfs(x, y, color, graph):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if graph[x][y] == color:
        graph[x][y] = 'X'
        dfs(x + 1, y, color, graph)
        dfs(x - 1, y, color, graph)
        dfs(x, y + 1, color, graph)
        dfs(x, y - 1, color, graph)
        return True

    return False

n = int(input())
graph1 = [list(input()) for _ in range(n)]
graph2 = [row[:] for row in graph1]

result = 0 
result_rg = 0

for i in range(n):
    for j in range(n):
        if graph1[i][j] != 'X':
            dfs(i, j, graph1[i][j], graph1)
            result += 1

for i in range(n):
    for j in range(n):
        if graph2[i][j] == 'R':
            graph2[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if graph2[i][j] != 'X':
            dfs(i, j, graph2[i][j], graph2)
            result_rg += 1

print(result)
print(result_rg)
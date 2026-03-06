# dfs 와 bfs
from collections import deque

def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=' ')

    for next in graph[v]:
        if not visited[next]:
            dfs(graph, visited, next)

def bfs(graph, visited, start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')

        for next in graph[v]:
            if not visited[next]:
                visited[next] = True
                q.append(next)


n, m, v = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 것부터 방문
for i in range(1, n+1):
    graph[i].sort()

dfs(graph, visited, v)

print()

visited = [False]*(n+1)

bfs(graph, visited, v)
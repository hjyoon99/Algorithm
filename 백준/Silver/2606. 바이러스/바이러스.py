# 2606 - 바이러스

import sys

def dfs(v):
    visited[v] = True

    for next in graph[v]:
        if not visited[next]:
            dfs(next)

input = sys.stdin.readline

com = int(input()) # 컴퓨터 수
pair = int(input()) # 컴퓨터 쌍의 수

graph = [[] for _ in range(com + 1)]
visited = [False] * (com + 1)
count = 0

for i in range(pair):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

dfs(1)

print(sum(visited) - 1)
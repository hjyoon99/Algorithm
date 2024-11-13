from collections import deque

# 노드의 개수
n = int(input())

# 그래프
graph = {i : [] for i in range(1, n+1)}

# 인접노드 정렬
for nodes in graph.values():
    nodes.sort()

# 트리 상 연결된 두 정점
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드의 부모를 구하라. -> 부모 정보 저장

def bfs(graph, start_node):
    parent = {start_node : None} # 1은 부모 없음
    need_visited = deque([start_node])
    visited = set([start_node])

    while need_visited:
        node = need_visited.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                need_visited.append(neighbor)

    
    return parent

sol = dict(sorted(bfs(graph, 1).items()))

for i in range(2, n+1):
    print(sol[i])

from collections import deque

# 입력
n, m, v = map(int, input().split())

# 그래프 초기화
graph = {i : [] for i in range(1, n+1)}

# 간선 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 인접 리스트 정렬 (정점 번호가 작은 순서부터 방문 위함)
for nodes in graph.values():
    nodes.sort()

# dfs
def dfs(graph, start_node):
    # 방문할 노드 저장하는 deque
    need_visited = deque([start_node])
    # 방문한 노드 저장
    visited = []

    while need_visited:
        node = need_visited.pop()

        if node not in visited:
            visited.append(node)

            # 현재 노드의 인접노드 삽입
            # 오른쪽에서 꺼내므로 역순으로 저장
            need_visited.extend(reversed(graph[node]))
        
    return visited

# bfs
def bfs(graph, start_node):
    need_visited = deque([start_node])
    visited = []

    while need_visited:
        node = need_visited.popleft()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])

    return visited

# DFS와 BFS 결과 출력
print(" ".join(map(str, dfs(graph, v))))
print(" ".join(map(str, bfs(graph, v))))
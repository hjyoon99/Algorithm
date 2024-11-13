from collections import deque


# 전체 사람 수 n (1 ~ n 번까지)
n = int(input())

# 촌수를 계산해야하는 서로 다른 두 사람의 번호
a, b = map(int, input().split())

# 부모 자식간 관계 개수 m
m = int(input())

# 관계 그래프 초기화
graph = { i :[] for i in range(1, n+1)}

# 부모 자식 간 관계 x(부모), y(자식)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 인접 리스트 정렬
for nodes in graph.values():
    nodes.sort()


# 촌수 나타내는 정수 출력, 전혀 관계 없으면 -1

def bfs(graph, start_node, target_node):
    level = 0
    # 방문 노드와 촌수 저장
    need_visited = deque([(start_node, 0)])
    visited = set()

    while need_visited:
        node, level = need_visited.popleft()
        if node == target_node:
            return level
        
        if node not in visited: #여기서 중복 체크
            visited.add(node)
            for neighbor in graph[node]:
                need_visited.append((neighbor, level+1))
        
    return -1

print(bfs(graph, a, b))
def dfs(node, visited, graph, n):
    visited[node] = True
    
    for next in range(n):
        if not visited[next] and graph[node][next] == 1:
            visited[next] = True
            dfs(next, visited, graph, n)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, computers, n)
            answer += 1
    return answer
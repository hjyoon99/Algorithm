def solution(n, wires):
    answer = n
    
    def dfs(node, graph, visited):
        visited[node] = True
        count = 1
        for next_node in graph[node]:
            if not visited[next_node]:
                count += dfs(next_node, graph, visited)
        return count
    
    for i in range(len(wires)):
        temp = wires[:i] + wires[i+1:]
        graph = [[] for _ in range(n+1)]
        
        for a, b in temp:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False]*(n+1)
        count = dfs(1, graph, visited)
        answer = min(answer, abs(n - 2*count))
    
    return answer
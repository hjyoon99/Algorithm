# 2667 단지 번호 붙이기

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if graph[x][y] == 1:
        count = 1
        graph[x][y] = 0
        count += dfs(x-1, y)
        count += dfs(x+1, y)
        count += dfs(x, y-1)
        count += dfs(x, y+1)
        return count
    return False

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

result = 0
count = 0
house = []

for i in range(n):
    for j in range(n):
        home = dfs(i, j)
        if home > 0:
            result += 1
            house.append(home)

house.sort()

print(result)
for h in house:
    print(h)
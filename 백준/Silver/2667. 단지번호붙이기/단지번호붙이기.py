# 단지 번호 붙이기

n = int(input())

apt = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    
    if apt[x][y] == 1:
        apt[x][y] = 0
        count = 1
        count += dfs(x-1, y)
        count += dfs(x+1, y)
        count += dfs(x, y-1)
        count += dfs(x, y+1)
    
        return count
    return 0

result = []
for i in range(n):
    for j in range(n):
        if apt[i][j] == 1:
            result.append(dfs(i, j))

print(len(result))
result.sort()
for i in result:
    print(i)
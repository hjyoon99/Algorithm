# n과 m 1

n, m = list(map(int, input().split()))

nums = list(map(int, input().split()))
nums.sort()

visited = [False] * 10001
arr = []

def dfs():
    if len(arr) == m:
        print(*arr)
        return
    for i in nums:
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs()
            arr.pop()
            visited[i] = False
            
dfs()
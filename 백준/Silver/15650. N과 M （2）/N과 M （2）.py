n, m = map(int, input().split())

# 1부터 n까지 중복없이 m개 고른 수열

result = []
visited = [False] * (n+1)

def back(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(start, n+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            back(i+1)
            result.pop()
            visited[i] = False

back(1)
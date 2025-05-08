n, m = map(int,input().split())
#1부터 n까지 자연수 중에서 중복 없이 m개를 고른 수열

#방문기록
visited = [False] * (n+1)
result = []

def back():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            back()
            result.pop()
            visited[i] = False
back()
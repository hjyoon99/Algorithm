n, m = map(int, input().split())

# 같은 수를 여러번 골라도 됨
# 수열은 비내림차순

result = []
visited = [False]*(n-1)

def back(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(start, n+1):
        result.append(i)
        back(i)
        result.pop()
back(1)
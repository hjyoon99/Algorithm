# 컴퓨터의 수
com  = int(input())

# 컴퓨터 쌍의 수 
com_pair = int(input())

# 바이러스 감염 컴퓨터
count = 0

# 인접 리스트
coms = [[] for _ in range(com+1)]

for _ in range(com_pair):
    a, b = map(int, input().split())

    coms[a].append(b)
    coms[b].append(a)

# 방문 여부 기록
visited = [False] * (com + 1)

def dfs(v):
    global count
    visited[v] = True # 현재 컴퓨터 방문처리
    count += 1 

    for i in coms[v]: # 연결 컴퓨터 탐색
        if not visited[i]: # 방문하지 않은 컴퓨터 있으면 재귀 호출
            dfs(i)

dfs(1)

# 1을 제외한 감염 컴퓨터 수 
print(count-1)
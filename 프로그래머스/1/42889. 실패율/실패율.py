def solution(N, stages):
    answer = list(range(1, N+1))
    fails = {}
    for stage in range(1,N+1):
        # 각 스테이지 별 분모
        botttom = sum(1 for x in stages if x >= stage)
        # 각 스테이지 별 분자
        top = sum(1 for x in stages if x == stage)
        # 각 스테이지 별 실패율
        fails[stage] = top / botttom if botttom != 0 else 0
    
    answer = sorted(answer,key=lambda x: (-fails[x], x))
    
    return answer
def solution(k, score):
    answer = []
    tmp = []
    
    for i in range(len(score)):
        # 현재 점수를 임시 배열에 추가
        tmp.append(score[i])
        tmp.sort()  # 정렬
        
        # k개의 점수를 유지하기 위해 초과된 부분 제거
        if len(tmp) > k:
            tmp.pop(0)
        
        # tmp 배열에서 최솟값을 결과에 추가
        answer.append(tmp[0])
    
    return answer

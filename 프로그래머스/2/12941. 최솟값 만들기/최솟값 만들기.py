def solution(A,B):
    answer = 0

    # 누적 곱이 최소가 되려면? -> 
    # 가장 큰 것 * 가장 작은 것
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer
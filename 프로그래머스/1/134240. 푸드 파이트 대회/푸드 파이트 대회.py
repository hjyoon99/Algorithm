def solution(food):
    answer = ''
    for i in range(1, len(food)):
        if(food[i]//2 >= 1):
            answer += str(i) * (food[i]//2)

    tmp = answer[::-1]
    answer += '0'
    answer += tmp
    
    return answer
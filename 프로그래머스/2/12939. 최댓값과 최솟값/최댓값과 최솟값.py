def solution(s):
    num = list(map(int, s.split(' '))) 
    mx = max(num)
    mn = min(num)
    answer = ''
    answer += str(mn)
    answer += ' '
    answer += str(mx)
    return answer
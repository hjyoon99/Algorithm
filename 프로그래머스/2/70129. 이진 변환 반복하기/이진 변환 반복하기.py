def solution(s):
    count = 0
    count_zero = 0
    answer = []
    
    while (s != '1'):
        count_zero += s.count('0')
        s = s.replace('0', '')
        s = format(len(s), 'b')
        count += 1
    return [count, count_zero]
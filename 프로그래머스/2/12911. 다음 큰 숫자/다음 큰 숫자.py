def solution(n):
    answer = 0
    big = n+1
    while(n < big):
        if (format(n, 'b').count('1') == format(big, 'b').count('1')):
            return big
        else:
            big += 1

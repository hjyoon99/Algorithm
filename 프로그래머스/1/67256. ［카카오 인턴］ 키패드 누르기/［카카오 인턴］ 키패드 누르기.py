def solution(numbers, hand):
    answer = ''
    
    pos = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    
    # 처음 왼손은 '*', 오른손은 '#'에
    tmp_L = '*'
    tmp_R = '#'
    
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            tmp_L = n
        elif n in [3, 6, 9]:
            answer += 'R'
            tmp_R = n
        else:
            # 현재 손가락 위치와 누를 번호의 (행, 열) 좌표 가져오기
            lr, lc = pos[tmp_L]
            rr, rc = pos[tmp_R]
            tr, tc = pos[n]
            
            # 맨해튼 거리 공식: |행 차이| + |열 차이|
            dist_L = abs(lr - tr) + abs(lc - tc)
            dist_R = abs(rr - tr) + abs(rc - tc)
            
            if dist_L == dist_R:
                if hand == 'right':
                    answer += 'R'
                    tmp_R = n
                else:
                    answer += 'L'
                    tmp_L = n
            elif dist_L > dist_R:
                answer += 'R'
                tmp_R = n
            else:
                answer += 'L'
                tmp_L = n
    return answer
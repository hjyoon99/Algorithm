from collections import deque

def solution(board, moves):
    bucket = deque()
    answer = 0
    
    for m in moves:
        for b in board:
            if b[m-1] > 0:
                if bucket and bucket[-1] == b[m-1]:
                    bucket.pop()
                    answer += 2
                else: bucket.append(b[m-1])
                b[m-1] = 0
                break
    return answer
        
    
    
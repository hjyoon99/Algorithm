def solution(name):
    count = 0
    n = len(name)
    # AAA로 시작
    for i in range(len(name)):
        # ord(name[i]) - ord('A') <= M
        if (ord(name[i]) - ord('A')) <= 13:
            count += ord(name[i]) - ord('A')
        
        else:
            count += ord('Z') - ord(name[i]) + 1
            
        # 좌우 이동
        min_move = n - 1
        for i in range(n):
            next_idx = i + 1
            while next_idx < n and name[next_idx] == 'A':
                next_idx += 1
            min_move = min(
                min_move,
                i * 2 + n - next_idx,
                i + 2 * (n - next_idx)
            )
        
    return count + min_move
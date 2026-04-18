def solution(video_len, pos, op_start, op_end, commands):
    mm, ss = map(int, pos.split(":"))
    current_pos = mm * 60 + ss
    vm, vs = map(int, video_len.split(":"))
    video_pos = vm * 60 + vs
    stm, sts = map(int, op_start.split(":"))
    em, es = map(int, op_end.split(":"))
    start = stm * 60 + sts
    end = em * 60 + es
    if ((current_pos >= start) and (current_pos <= end)):
            current_pos = end
    
    for command in commands:
    
        if ((current_pos >= start) and (current_pos <= end)):
            current_pos = end

        if command == 'prev':
            current_pos -= 10
            current_pos = max(current_pos, 0)

        if command == 'next':
            current_pos += 10
            current_pos = min(current_pos, video_pos)
            
        if ((current_pos >= start) and (current_pos <= end)):
            current_pos = end
    
    # 시간 변환
    m = current_pos // 60
    s = current_pos % 60
    print(current_pos)
    return f"{m:02d}:{s:02d}"
    
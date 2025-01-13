def solution(cards1, cards2, goal):
    
    for g in goal:
        if cards1 and g == cards1[0]:
            #일치하면 요소 삭제
            del cards1[0]
        elif cards2 and g == cards2[0]:
            del cards2[0]
        else:
            return "No"
    return "Yes"
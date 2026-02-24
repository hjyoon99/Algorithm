from itertools import permutations

def solution(k, dungeons):
    answer = -1
    # 현재피로도 = k
    # 하루 한번씩 탐험 가능한 던전을 최대한 많이
    perm = permutations(dungeons, len(dungeons))
    for p in perm:
        count = 0
        piro = k
        for dun in p:
            minimum = dun[0]
            use = dun[1]
            # if k >= 최소피로도
            if piro >= minimum:
                count += 1
                # 피로도 -= 소모 피로도
                piro -= use
            else:
                break
        answer = max(answer, count)
    return answer
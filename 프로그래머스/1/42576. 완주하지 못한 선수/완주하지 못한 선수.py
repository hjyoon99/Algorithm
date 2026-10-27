def solution(participant, completion):
    part = {}
    for p in participant:
        part[p] = part.get(p, 0) + 1
    for c in completion:
        if c in part:
            part[c] -= 1
    filtered = [k for k, v in part.items() if v >= 1]
    return filtered[0]
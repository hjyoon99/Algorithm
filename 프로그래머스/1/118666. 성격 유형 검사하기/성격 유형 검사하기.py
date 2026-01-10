def solution(survey, choices):
    answer = ''
    score = {
        "R" : 0, "T" : 0,
        "C" : 0, "F" : 0,
        "J" : 0, "M" : 0,
        "A" : 0, "N" : 0
    }
    for i in range(len(survey)):
        a, b = survey[i][0], survey[i][1]
        if choices[i] < 4:
            score[a] += 4 - choices[i]
        elif choices[i] > 4:
            score[b] += choices[i] - 4
        
    for x, y in [('R','T'), ('C','F'), ('J','M'), ('A','N')]:
        if score[x] >= score[y]:
            answer += x
        else:
            answer += y
    
    
    return answer
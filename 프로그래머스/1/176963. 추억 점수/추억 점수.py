def solution(name, yearning, photo):
    answer = []
    
    longing = {}
    for i in range(len(name)):
        longing[name[i]] = yearning[i]
    
    for pho in photo:
        count = 0
        for j in range(len(pho)):
            if(pho[j] in name):
                count += longing[pho[j]]
        answer.append(count)
    return answer
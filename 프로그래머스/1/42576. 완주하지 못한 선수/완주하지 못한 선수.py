def solution(participant, completion):
    
    participation = {}
    for person in participant:
        participation[person] = participation.get(person, 0) + 1
    
    for person in completion:
        participation[person] -= 1
    
    for k, v in participation.items():
        if v > 0:
            return k

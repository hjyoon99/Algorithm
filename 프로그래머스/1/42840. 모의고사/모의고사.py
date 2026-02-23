def solution(answers):
    answer = []
    # 1번 ->  12345
    # 2번 -> 21 23 24 25
    # 3번 -> 33 11 22 44 55
    
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    n1 = 0
    n2 = 0
    n3 = 0
    
    for i in range(len(answers)):
        if answers[i] == num1[i % 5]:
            n1 += 1
        if answers[i] == num2[i % 8]:
            n2 += 1
        if answers[i] == num3[i % 10]:
            n3 += 1
    
    answer = [n1, n2, n3]
    max_val = max(answer)
    max_idxes = [i + 1 for i, v in enumerate(answer) if v == max_val]
    
    max_idxes.sort()
    
    return max_idxes
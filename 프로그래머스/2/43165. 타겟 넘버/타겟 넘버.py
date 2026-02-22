def solution(numbers, target):
    answer = 0
    
    def dfs(index, total):
        nonlocal answer
        
        if index == len(numbers):
            if total == target:
                answer += 1
            return
        
        # + 선택
        dfs(index + 1, total + numbers[index])

        # - 선택
        dfs(index + 1, total - numbers[index])
        
    dfs(0, 0)
    return answer
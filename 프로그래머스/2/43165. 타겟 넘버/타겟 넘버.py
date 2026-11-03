def solution(numbers, target):
    def dfs(idx, total):
        if idx == len(numbers):
            return 1 if total == target else 0
        
        plus = dfs(idx+1, total + numbers[idx])
        minus = dfs(idx+1, total - numbers[idx])
        
        return plus + minus
    return dfs(0, 0)
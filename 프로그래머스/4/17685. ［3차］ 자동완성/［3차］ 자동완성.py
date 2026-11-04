def solution(words):
    words.sort()
    
    def lcp(a, b):
        count = 0
        
        for x, y in zip(a, b):
            if x != y:
                break
            count += 1
        return count
    
    answer = 0
    n = len(words)
    
    for i in range(n):
        prev = lcp(words[i-1], words[i]) if i > 0 else 0
        next_ = lcp(words[i], words[i+1]) if i < n-1 else 0
        
        answer += min(len(words[i]), max(prev, next_) + 1)
    return answer
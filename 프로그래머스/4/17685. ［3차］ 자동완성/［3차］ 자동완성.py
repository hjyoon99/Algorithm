class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

def solution(words):
    root = TrieNode()
    
    # Trie에 단어 삽입
    for word in words:
        node = root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                
            node = node.children[char]
            node.count += 1
    # 각 단어 최소 입력 횟수 계산
    answer = 0
    
    for word in words:
        node = root
        
        for char in word:
            node = node.children[char]
            answer += 1
            
            if node.count == 1:
                break
    return answer
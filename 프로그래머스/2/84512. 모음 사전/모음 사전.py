from itertools import product

def solution(word):
    count = 0
    words = []
    dictionary = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(1, 6):
        perm = list(product(dictionary, repeat=i))
        for p in perm:
            words.append(''.join(p))
        
    words.sort()
    
    return words.index(word) + 1
def solution(s):
    words = s.split(' ')
    words = [w.capitalize() for w in words]
    return ' '.join(words)
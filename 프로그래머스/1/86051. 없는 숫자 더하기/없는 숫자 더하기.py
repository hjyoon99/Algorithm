def solution(numbers):
    s = 0
    for i in range(0, 10):
        if i not in numbers:
            s += i
    return s
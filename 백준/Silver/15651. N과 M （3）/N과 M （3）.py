n ,m = map(int, input().split())

result = []

def back():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        result.append(i)
        back()
        result.pop()
back()
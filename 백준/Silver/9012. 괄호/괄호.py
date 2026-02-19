# 9012 괄호
n = int(input())

for _ in range(n):
    ps = input()
    stack = []
    for s in ps:
        if stack and stack[0] == ')':
            break
        elif stack and stack[-1] != s:
            stack.pop()
        else: 
            stack.append(s)
    if stack:
        print('NO')
    else:
        print('YES')
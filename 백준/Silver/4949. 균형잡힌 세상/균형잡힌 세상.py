# 4949 균형잡힌 세상
while True:
    s = input()

    if s == '.':
        break

    stack = []
    balanced = True

    for ch in s:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                balanced = False
                break
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                balanced = False
                break
    if balanced and not stack:
        print('yes')
    else:
        print('no')
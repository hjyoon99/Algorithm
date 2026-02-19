#12789 - 도키도키 간식드리미
n = int(input())
line = list(map(int, input().split()))

stack = []
next_num = 1

for student in line:
    if student == next_num:
        next_num += 1

        while stack and stack[-1] == next_num:
            stack.pop()
            next_num += 1
    else:
        stack.append(student)

if not stack:
    print('Nice')
else:
    print('Sad')
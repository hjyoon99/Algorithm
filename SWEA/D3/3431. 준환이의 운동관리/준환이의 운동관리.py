def exer(x):
    if l <= x <= u:
        return 0
    if x > u:
        return -1
    else:
        return l - x

t = int(input())
for tc in range(1, t+1):
    l, u, x = map(int, input().split())

    print(f'#{tc} {exer(x)}')
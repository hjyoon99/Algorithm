t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    homeworks = list(map(int, input().split()))

    result = []

    for i in range(1, n+1):
        if i not in homeworks:
            result.append(i)
    sol = ' '.join(map(str, result))

    print(f'#{tc} {sol}')
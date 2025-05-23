t = int(input())  # 테스트 케이스 수
for tc in range(1, 1 + t):
    n = int(input())
    cards = list(map(str, input().split()))

    result = ['0'] * n

    # 입력값이 짝수일때
    i = 0
    j = 1

    if n % 2 == 0:
        for k in range(n//2):
            result[i] = cards[k]
            i += 2
        for l in range(n//2, n):
            result[j] = cards[l]
            j += 2
    else:
        for m in range(n//2 + 1):
            result[i] = cards[m]
            i += 2
        for s in range(n//2+1, n):
            result[j] = cards[s]
            j += 2

    sol = ' '.join(map(str, result))
    print(f'#{tc} {sol}')
t = int(input())  # 테스트 케이스 수
for tc in range(1, 1 + t):
    n = list(map(int, input().split()))

    sol = round(sum(n) / 10)

    print(f'#{tc} {sol}')
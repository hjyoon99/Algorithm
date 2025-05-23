t = int(input())  # 테스트 케이스 수
for tc in range(1, 1 + t):
    n = int(input())

    count = 0

    if n < 3:
        count = 0
    else:
        count = n // 3

    print(f'#{tc} {count}')

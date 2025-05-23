t = int(input())  # 테스트 케이스 수
for tc in range(1, 1 + t):
    n, d = map(int, input().split())  # n: 전체 칸 수, d: 좌우로 덮는 범위

    size = 2*d + 1
    count = 0
    if (n % size) == 0:
        count = n // size
    else:
        count = n // size + 1

    print(f'#{tc} {count}')

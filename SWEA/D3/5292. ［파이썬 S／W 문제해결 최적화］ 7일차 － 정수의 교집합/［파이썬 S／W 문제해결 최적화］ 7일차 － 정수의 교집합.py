t = int(input())  # 테스트 케이스 수
for tc in range(1, 1 + t):
    n, m = map(int, input().split())

    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))

    set_a = set(list_a)
    set_b = set(list_b)

    result = set_a & set_b

    print(f'#{tc} {len(result)}')
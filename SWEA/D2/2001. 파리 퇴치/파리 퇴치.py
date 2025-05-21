t = int(input())
for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    boards = [list(map(int, input().split())) for _ in range(n)]

    max_result = 0

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            total = 0
            for x in range(m):
                for y in range(m):
                    total += boards[i+x][j+y]
                max_result = max(max_result, total)

    print(f'#{test_case} {max_result}')
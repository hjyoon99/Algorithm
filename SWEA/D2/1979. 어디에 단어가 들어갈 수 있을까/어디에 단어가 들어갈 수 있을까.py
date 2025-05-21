t = int(input())

for test_case in range(1, t+1):
    n, k = map(int, input().split())
    boards = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    # 길이가 k 가로 검색
    for i in range(n):
        check_one = 0
        for j in range(n):
            if boards[i][j] == 1:
                check_one += 1

            else:
                if check_one == k:
                    result += 1
                check_one = 0

        if check_one == k:
            result += 1

    # 세로 검색
    for l in range(n):
        check_one = 0
        for m in range(n):
            if boards[m][l] == 1:
                check_one += 1
            else:
                if check_one == k:
                    result += 1
                check_one = 0

        if check_one == k:
            result += 1

    print(f'#{test_case} {result}')
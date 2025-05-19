t = 10
for test_case in range(1, t+1):
    test = int(input())
    n, m = map(int, input().split())

    result = 1

    for i in range(m):
        result *= n

    print(f'#{test} {result}')
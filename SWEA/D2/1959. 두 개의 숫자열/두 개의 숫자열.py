t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if len(a) > len(b):
        a, b = b, a

    max_sum = float('-inf')
    for i in range(len(b) - len(a) +1):
        tmp = 0
        for j in range(len(a)):
            tmp += a[j] * b[i+j]
        max_sum = max(max_sum, tmp)

    print(f'#{test_case} {max_sum}')

def dfs(idx, current_sum):
    global count
    if current_sum > k:
        return
    if idx == n:
        if current_sum == k:
            count += 1
        return
    dfs(idx+1, current_sum + list_a[idx])
    dfs(idx+1, current_sum)

t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    list_a = list(map(int, input().split()))

    count = 0
    dfs(0, 0)

    print(f'#{test_case} {count}')
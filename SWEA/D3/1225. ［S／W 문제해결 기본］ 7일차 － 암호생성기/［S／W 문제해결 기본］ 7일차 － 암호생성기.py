from collections import deque

def cyper(nums):
    q = deque(nums)

    while q:
        for i in range(1, 6):
            n = q.popleft()
            if n-i > 0:
                q.append(n-i)
            else:
                q.append(0)
                return q

t = 10
for test_case in range(1, t+1):
    _ = int(input())
    nums = list(map(int, input().split()))

    result_list = list(cyper(nums))
    result = ' '.join(map(str,result_list))

    print(f'#{test_case} {result}')
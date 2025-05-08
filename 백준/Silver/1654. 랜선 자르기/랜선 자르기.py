# 만들 수 있는 최대 길이의 랜선

def binary_search(arr, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for line in arr:
            count += line // mid
        if count >= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]
lines.sort()

print(binary_search(lines, n, 1, max(lines)))
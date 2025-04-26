def binary_search(array, target, start, end):
    while start <= end:
        total = 0
        mid = (start + end) // 2
        if total == target:
            return mid
        for arr in array:
            if arr > mid:
                total += (arr - mid)
        if total < target:
            end = mid - 1
        else:
            start = mid + 1
            result = mid
    return result

n, m = map(int, input().split())
array = list(map(int, input().split()))
print(binary_search(array, m, 0, max(array)))
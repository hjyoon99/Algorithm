def binary_search(arr1, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr1[mid] == target:
        return 1
    elif arr1[mid] < target:
        return binary_search(arr1, target, mid+1, end)
    else:
        return binary_search(arr1, target, start, mid-1)
            

# 테스트케이스 수
t = int(input())
for _ in range(t):
    # 수첩1
    n = int(input())
    arr1 = list(map(int, input().split()))
    # 수첩2
    m = int(input())
    arr2 = list(map(int, input().split()))

    arr1.sort()

    for a2 in arr2:
        target = a2
        print(binary_search(arr1, target, 0, n-1))
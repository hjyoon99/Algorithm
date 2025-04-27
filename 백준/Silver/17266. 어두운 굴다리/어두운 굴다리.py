def is_possible(H, array, n):
    # 첫 구간
    if array[0] - H > 0:
        return False
    
    # 각 구간 사이
    for i in range(1, len(array)):
        if array[i] - array[i-1] > 2 * H:
            return False
    
    # 마지막 구간
    if array[-1] + H < n:
        return False
    return True

def binary_search(array, start, end):
    result = -1
    while start <= end:
        mid = (start+end) // 2
        if is_possible(mid, array, n):
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result


n = int(input())  # 굴다리 길이
m = int(input())  # 가로등 개수
place = list(map(int, input().split()))  # 가로등 위치

print(binary_search(place, 0, n))
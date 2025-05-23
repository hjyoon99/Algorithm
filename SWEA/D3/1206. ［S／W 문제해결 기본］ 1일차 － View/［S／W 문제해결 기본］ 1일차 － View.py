for tc in range(1, 11):
    n = int(input())
    buildings = list(map(int, input().split()))

    count = 0

    for i in range(2, n-2):
        left = max(buildings[i-2], buildings[i-1])
        right = max(buildings[i+2], buildings[i+1])

        height = max(left, right)

        if buildings[i] >= height:
            count += buildings[i] -height



    print(f'#{tc} {count}')
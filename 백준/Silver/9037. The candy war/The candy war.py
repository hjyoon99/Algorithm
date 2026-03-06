# the candy war

t = int(input())

for _ in range(t):
    n = int(input())


    # 사탕의 초기값
    children = list(map(int, input().split()))
    count = 0

    # 처음 홀수 처리
    for i in range(n):
        if (children[i] % 2) != 0:
            children[i] += 1

    while True:
        # 같은지 확인
        if len(set(children)) == 1:
            break

        # 반 나눠서 오른쪽 전달
        give = [candy // 2 for candy in children]

        for i in range(n):
            children[i] = (children[i] // 2) + give[i-1]
            
        # 홀수면 +1
        for i in range(n):
            if (children[i] % 2) != 0:
                children[i] += 1

        count += 1

    print(count)
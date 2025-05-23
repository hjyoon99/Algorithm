t = int(input())
for tc in range(1, t+1):
    #반지름
    n = int(input())

    count = 0

    for i in range(-n, n+1):
        for j in range(-n, n+1):
            if i*i + j*j <= n*n:
                count += 1
    print(f'#{tc} {count}')
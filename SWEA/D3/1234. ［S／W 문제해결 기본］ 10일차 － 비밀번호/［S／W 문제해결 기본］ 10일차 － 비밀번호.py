t = 10
for test_case in range(1, t+1):
    n, string = map(str, input().split())
    n = int(n)
    st = list(string)
    i = 0

    while i < len(st) - 1:
        if st[i] == st[i+1]:
            del st[i:i+2]
            if i > 0:
                i -= 1
        else:
            i += 1

    result = ''.join(map(str, st))
    
    
    print(f'#{test_case} {result}')
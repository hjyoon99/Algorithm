import sys

# 테스트케이스
t = int(input())

# 케이스 입력받고 리스트로 저장
a = [sys.stdin.readline().strip() for _ in range(t)]

# 리스트 순회, 초기화
for i in range(t):
    s = int(a[i]) # 
    q = 0
    d = 0
    n = 0
    p = 0

    while(True): 

        if (s // 25) > 0: 
            q = s // 25 
            s -= 25 * (s // 25) 
            continue
        
        elif (s // 10) > 0:
            d = s // 10
            s -= 10 * (s // 10)
            continue
        
        elif (s // 5) > 0:
            n = s // 5
            s -= 5 * (s // 5)
            continue
        
        else:
            p = s // 1 # 0
            s -= 1 * (s // 1)

            break
    
    print(q, d, n ,p)
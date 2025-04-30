from bisect import bisect_right

#테스트케이스 (주의!!)
t = int(input())

for i in range(t): #테스트케이스만큼 반복
    a, b = list(map(int, input().split()))
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    list_b.sort()

    count = 0
    for l_a in list_a:
        count += bisect_right(list_b, l_a-1)
    print(count)
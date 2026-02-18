n = int(input())

a = list(map(int,input().split(" ")))
b = list(map(int,input().split(" ")))

# 가장 작은 친구 * 가장 큰 친구

a.sort()
b.sort(reverse = True)

total = 0

for i in range(n):
    total += a[i] * b[i]

print(total)
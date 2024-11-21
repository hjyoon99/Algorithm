n = int(input())
p = list(map(int, input().split()))
count = 0

k = n

sorted_p = sorted(p)

for i in range(n):
    count += (sorted_p[i] * k)
    k -= 1

print(count)
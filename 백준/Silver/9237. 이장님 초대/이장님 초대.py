n = int(input())

tree = list(map(int, input().split()))

tree.sort(reverse=True)
max_day = 0

for i in range(n):
    grow_day = (i + 1) + tree[i]
    max_day = max(max_day, grow_day)

print(max_day + 1)
n = int(input())
max_ns = []

for i in range(n):
    max_n = int(input())
    max_ns.append(max_n)

sorted_max_ns = sorted(max_ns)
max_weight = 0
tmp = n

for j in range(n):
    weight = sorted_max_ns[j] * tmp
    if weight > max_weight:
        max_weight = weight
    tmp -= 1

print(max_weight)
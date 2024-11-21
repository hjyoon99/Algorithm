n = int(input())
max_ns = [int(input()) for _ in range(n)]

max_ns.sort()
max_weight = max(max_ns[i] * (n-i) for i in range(n))

print(max_weight)
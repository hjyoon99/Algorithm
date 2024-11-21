# n 개의 로프
# k 개의 로프 사용해 중량 w인 물체 ->  *고르게* w/k 만큼의 중량
# 들어올릴 수 있는 최대 중량
# 임의로 로프 골라도 됨

n = int(input())
max_ns = []

for i in range(n):
    max_n = int(input())
    max_ns.append(max_n)

sorted_max_ns = sorted(max_ns)
weights = []
tmp = n

for j in range(n):
    weight = sorted_max_ns[j] * tmp
    weights.append(weight)
    tmp -= 1

print(max(weights))
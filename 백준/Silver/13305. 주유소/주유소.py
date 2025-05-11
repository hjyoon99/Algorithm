city = int(input())
roads_length = list(map(int, input().split()))
oils = list(map(int, input().split()))

# 각 도시를 지날 때마다 현재까지 가장 싼 기름값으로만 계산해 나가는 방식.

total_cost = 0
min_oil = oils[0]

for i in range(city -1):
    if oils[i] < min_oil:
        min_oil = oils[i]
    total_cost += min_oil * roads_length[i]

print(total_cost)
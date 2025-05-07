n, k = map(int, input().split())

coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

count = 0

for i in range(n-1, -1, -1):
    if coins[i] <= k:
        use = k // coins[i]
        count += use
        k -= use * coins[i]
    if k == 0:
        break

print(count)
# rgb 

n = int(input())

dp = [[0] * 3 for _ in range(n+1)]
cost = [[0] * 3 for _ in range(n+1)]

for i in range(1, n+1):
    r, g, b = map(int, input().split())
    cost[i][0] = r
    cost[i][1] = g
    cost[i][2] = b

dp[1][0] = cost[1][0]
dp[1][1] = cost[1][1]
dp[1][2] = cost[1][2]


for j in range(2, n+1):
    
    dp[j][0] = cost[j][0] + min(dp[j-1][1], dp[j-1][2])
    dp[j][1] = cost[j][1] + min(dp[j-1][0], dp[j-1][2])
    dp[j][2] = cost[j][2] + min(dp[j-1][0], dp[j-1][1])

print(min(dp[n]))
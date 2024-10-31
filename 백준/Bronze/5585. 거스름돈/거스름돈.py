a = int(input())

#1000원짜리 한장 내면 받을 잔돈 개수

# 500, 100, 50, 10, 5, 1
# 최소잔돈
m = 1000 - a #a = 1, m = 999
sum = 0

while(True):

    if m // 500 > 0:
        sum += m // 500 # 1
        m -= 500*(m//500) # 999 - 500 * 1 = 499
        continue
    elif m//100 > 0: 
        sum += m // 100 # 1 + 4
        m -= 100*(m//100) # 499 - 100 * 4 = 99
        continue
    elif m//50 > 0: 
        sum += m // 50 # 1 + 4 + 1 
        m -= 50*(m//50) # 99 - 50 * 1 = 49
        continue
    elif m//10 > 0:
        sum += m// 10 #1 + 4 + 1 + 4
        m -= 10*(m//10) # 49 - 10 * 4 = 9
        continue
    elif m//5 > 0: 
        sum += m // 5 # 1 + 4 + 1 + 4 + 1
        m -= 5*(m//5) # 9 - 5 * 1 = 4
        continue
    else:
        sum += m // 1 # 1 + 4 + 1 + 4 + 1 + 4
        m -= m # 0 
        break

print(sum)
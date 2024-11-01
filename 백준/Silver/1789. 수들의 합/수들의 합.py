# 서로 다른 n개 자연수 합 입력
s = int(input())

sum = 0
count = 0

# 합이 정확이 200이 아니더라도, 작은 수부터 더해 최대 자연수 개수 찾는게 목표
for i in range(1, s+1):
    sum += i
    count += 1
    if sum > s:
        count -= 1
        break
print(count)
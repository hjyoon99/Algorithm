s = input()

count = 0

# 인접한 값이 다른 경우에만 카운트 증가
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        count += 1

# 최소 횟수는 변화 구간의 절반
result = (count + 1) // 2

print(result)
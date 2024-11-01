import sys

#회의 수
t = int(input())

time = []

# 케이스 입력
for _ in range(t):
    a, b = map(int, input().split())

    time.append((a, b))

# 끝나는 시간 기준 정렬, 끝나는 시간 같으면 시작 시간 기준 정렬
time_a= sorted(time, key=lambda x: (x[1], x[0]))

# 최대 회의 수
max = 0
end_time = 0

for a, b in time_a:
    # 이전 회의가 끝난 후 시작할 수 있는 회의만 선택
    if a >= end_time:
        max += 1
        end_time = b

print(max)
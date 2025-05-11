# 연산자 끼워넣기

# 연산자 우선 순위 무시하고 앞에서부터 계산
# 나눗셈은 정수 몫만 취한다
# 음수는 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다

# N개의 수와 N-1개의 연산자가 주어졌을 때 만들 수 있는 식의 결과가 최대, 최소?

n = int(input())
list_a = list(map(int, input().split()))
# 0번째 : +, 1번째 : -, 2번째: *, 3번째: // 개수
operators = list(map(int, input().split()))

max_result = -float('inf')
min_result = float('inf')

# 숫자 리스트는 고정
# 연산지 하나씩 선택하며 순서대로 수 계산
# 연산자 개수 하나씩 줄여가며 재귀
# 깊이가 n-1이면 숫자 사용 완료 -> 결과 저장

def back(idx, current):
    global max_result, min_result

    if idx == n:
        max_result = max(max_result, current)
        min_result = min(min_result, current)
        return
    
    for i in range(4): #operator 위치 순회
        if operators[i] > 0:
            operators[i] -= 1 # 개수 하나씩 빼기

            next_val = 0
            if i == 0:
                next_val = current + list_a[idx]
            elif i == 1:
                next_val = current - list_a[idx]
            elif i == 2:
                next_val = current * list_a[idx]
            else:
                if current < 0:
                    next_val = -(-current // list_a[idx])
                else:
                    next_val = current // list_a[idx]
            
            back(idx+1, next_val)
            operators[i] += 1 # 되돌리기

back(1, list_a[0])

print(max_result)
print(min_result)
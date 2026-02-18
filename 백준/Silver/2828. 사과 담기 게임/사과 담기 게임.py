n, m = map(int, input().split(" "))
j = int(input())
left = 1
right = m
move = 0

for _ in range(j):
    apple = int(input())

    # 사과가 왼쪽 이동
    if apple < left:
        diff = left - apple
        left -= diff
        right -= diff
        move += diff
 
    # 사과가 오른쪽 이동
    elif apple > right:
        diff = apple - right
        left += diff
        right += diff
        move += diff

print(move)
# 1193 - 분수찾기

x = int(input())

line = 1

# X가 몇번째 대각선일까? -> 누적합
while x > line:
    x -= line
    line += 1

if line % 2 == 0:
    num = x
    den = line - x + 1
else:
    num = line - x + 1
    den = x

print(f'{num}/{den}')
# 4158 - CD
import sys

input = sys.stdin.readline

while True:

    n, m = list(map(int, input().split()))

    if n == 0 and m == 0:
        break

    sk = set()
    count = 0

    for i in range(n):
        s = int(input())
        sk.add(s)

    for j in range(m):
        y = int(input())

        if y in sk:
            count += 1
    

    print(count)
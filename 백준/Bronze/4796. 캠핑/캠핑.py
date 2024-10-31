# L, P, V
# 연속하는 P일 중 L일 동안 사용, V일 휴가

import sys

a = []
count = 1

while(True):
    l, p, v =(map(int, input().split()))

    if l == 0 and p == 0 and v == 0:
        break

    a.append([l, p, v])

for d in a:
    if d[2]%d[1] < d[0]:
        s = (d[2] // d[1]) * d[0] + (d[2] % d[1])
    else:
        s = (d[2] // d[1]) * d[0] + d[0]
    print("Case {}:".format(count), s)
    count += 1
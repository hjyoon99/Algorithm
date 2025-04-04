t = int(input())

a = 300
b = 60
c = 10

count_a = 0
count_b = 0
count_c = 0

if (t % 10) != 0:
    print(-1)
else:
    while t != 0:
        if t >= a:
            count_a += (t // a)
            t %= a
        elif t >= b:
            count_b += (t // b)
            t %= b
        else:
            count_c += (t // c)
            t %= c
    print(count_a, count_b, count_c)
n, m = map(int, input().split())

test = []
count = 0

for _ in range(n):
    s = input()
    test.append(s)

for _ in range(m):
    string = input()
    if string in test:
        count += 1
print(count)
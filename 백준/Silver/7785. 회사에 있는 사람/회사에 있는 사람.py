# 현재 회사에 있는 모든 사람을 구하자.
n = int(input())

enter = set()

for i in range(n):
    name = input().split()
    if name[1] == 'enter':
        enter.add(name[0])
    else: 
        enter.remove(name[0])

for i in sorted(enter, reverse = True):
    print(i)

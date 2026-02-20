import sys
from collections import deque

input = sys.stdin.readline  # 빠른 입력

n = int(input())
queue = deque()
result = []  # 출력 모아두기

for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'push':
        queue.append(cmd[1])

    elif cmd[0] == 'pop':
        if queue:
            result.append(queue.popleft())
        else:
            result.append(-1)

    elif cmd[0] == 'size':
        result.append(len(queue))

    elif cmd[0] == 'empty':
        result.append(0 if queue else 1)

    elif cmd[0] == 'front':
        result.append(queue[0] if queue else -1)

    elif cmd[0] == 'back':
        result.append(queue[-1] if queue else -1)

print("\n".join(map(str, result)))

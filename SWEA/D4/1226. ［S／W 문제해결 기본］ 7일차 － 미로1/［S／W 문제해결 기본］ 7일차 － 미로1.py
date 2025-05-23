def find_road(x, y):
    visited[x][y] = True
    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    if maze[x][y] == 3:
        return 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 16 and 0 <= ny < 16:
            if not visited[nx][ny] and maze[nx][ny] != 1:
                if find_road(nx, ny):
                    return 1

    return 0


for test_case in range(10):
    t = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    visited = [[False] * 16 for _ in range(16)]

    print(f'#{t} {find_road(1, 1)}')
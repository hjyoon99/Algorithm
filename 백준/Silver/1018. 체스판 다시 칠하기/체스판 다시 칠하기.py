def count_square(x, y):
    colors = ['W', 'B']
    min_count = float('inf')

    for first in colors:
        count = 0
        for i in range(8):
            for j in range(8):
                expected = first if (i+j)%2 == 0 else ('W' if first == 'B' else 'B')

                if matrix[x+i][y+j] != expected:
                    count += 1
        min_count = min(min_count, count)

    return min_count

n, m = map(int, input().split())

matrix = [list(input().strip()) for _ in range(n)]

answer = float('inf')
for i in range(n-7):
    for j in range(m-7):
        answer = min(answer, count_square(i, j))

print(answer)
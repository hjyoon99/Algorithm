def is_palindrom(word):
    return word == word[::-1]

t = 10
for test_case in range(1, t + 1):
    t = int(input())  # 테스트 케이스 번호 입력 (무시해도 됨)
    board = [list(input()) for _ in range(100)]
    max_length = 0

    for length in range(100, 0, -1):  # 긴 길이부터 먼저 검사
        found = False

        # 가로 검사
        for i in range(100):
            for j in range(100 - length + 1):
                if is_palindrom(board[i][j:j + length]):
                    max_length = length
                    found = True
                    break
            if found:
                break

        if found:
            break

        # 세로 검사
        for j in range(100):
            for i in range(100 - length + 1):
                temp = [board[x][j] for x in range(i, i + length)]
                if is_palindrom(temp):
                    max_length = length
                    found = True
                    break
            if found:
                break
        if found:
            break

    print(f"#{t} {max_length}")
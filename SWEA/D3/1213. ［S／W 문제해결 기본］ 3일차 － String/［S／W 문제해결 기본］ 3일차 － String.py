t = 10
for test_case in range(1, t+1):
    test = int(input())
    word = str(input())
    string = str(input())

    count = 0
    # string에서 word의 개수 반환
    for i in range(len(string)):
        if string[i:i+len(word)] == word:
            count += 1
        
    print(f'#{test} {count}')
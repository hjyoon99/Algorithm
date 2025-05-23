def choose(nums, idx, path, result):
    if len(path) == 3:
        result.add(sum(path))
        return
    if idx >= len(nums):
        return

    # 현재 숫자 선택
    choose(nums, idx + 1, path + [nums[idx]], result)

    # 현재 숫자 선택 안 함
    choose(nums, idx + 1, path, result)




t = int(input())  # 테스트 케이스 수
for tc in range(1, 1 + t):
    nums = list(map(int, input().split()))
    result = set()  # 중복 제거를 위해 set 사용
    choose(nums, 0, [], result)

    result = sorted(result, reverse= True)  # 내림차순 정렬
    print(f'#{tc} {result[4]}')  # 5번째로 큰 값 출력
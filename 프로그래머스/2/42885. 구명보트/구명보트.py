def solution(people, limit):
    people.sort()
    count = 0
    # 한 보트에 2명씩
    # 무게 제한 limit
    # 50 50 70 80
    left = 0
    right = len(people) - 1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        count += 1
    
    # 구명 보트 개수 최솟값
    return count
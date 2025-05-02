def binary_search(array, target, start, end):
    max_length = 0
    
    while start <= end:
        mid = (start +  end) // 2
        
        count = sum(snack // mid for snack in array)

        if count >= target:
            max_length = mid
            start = mid + 1
        else:
            end = mid - 1
        
    return max_length



sibling, snk_count = list(map(int, input().split()))
snacks = list(map(int, input().split()))
snacks.sort()

result = binary_search(snacks, sibling, 1, max(snacks))
print(result)
def solution(nums):
    pick_num = len(nums) // 2
    set_nums = set(nums)
    
    return min(pick_num, len(set_nums))  
# 셀프 넘버
# 10000보다 작거나 같은 셀프 넘버

nums = [True] * 10001
for i in range(1, 10000):
    tmp = list(map(int,str(i)))
    total = i
    for n in tmp:
        total += n
    if total <= 10000:
        nums[total] = False


for j in range(1, 10000):
    if nums[j]:
        print(j)


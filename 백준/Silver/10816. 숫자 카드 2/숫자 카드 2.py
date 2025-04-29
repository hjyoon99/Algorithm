from bisect import bisect_left, bisect_right

def bisect_count(arr, right, left):
    right_val = bisect_right(arr, right)
    left_val = bisect_left(arr, left)
    return right_val - left_val


n = int(input())
sk_card = list(map(int, input().split()))
sk_card.sort()

m = int(input())
cards = list(map(int, input().split()))

for c in cards:
    print(bisect_count(sk_card, c, c), end= ' ')
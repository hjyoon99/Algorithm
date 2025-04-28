def find_number_card(arr, target, start, end):
    mid = (start + end) // 2
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

n = int(input())
sk_cards = list(map(int, input().split()))
sk_cards.sort()

m = int(input())
cards = list(map(int, input().split()))

for card in cards:
    print(find_number_card(sk_cards, card, 0, n-1), end = ' ')
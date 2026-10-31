def solution(sizes):
    return max(max(card) for card in sizes) * max(min(card) for card in sizes)
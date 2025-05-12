strings = input().split('-')

first = sum(map(int, strings[0].split('+')))

for part in strings[1:]:
    first -= sum(map(int, part.split('+')))

print(first)
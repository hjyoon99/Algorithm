n = int(input())

count = 0

for i in range(n):
    string = input()
    ok = []
    is_group = True

    for j in range(len(string)):
        if string[j] not in ok:
            ok.append(string[j])
        else:
            if j > 0 and string[j] != string[j - 1]:
                is_group = False
                break
    if is_group:
        count += 1
print(count)
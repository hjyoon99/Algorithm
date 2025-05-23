for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for i in range(dump):
        max_box = boxes.index(max(boxes))
        min_box = boxes.index(min(boxes))
        boxes[max_box] -= 1
        boxes[min_box] += 1


    result = max(boxes) - min(boxes)

    print(f'#{tc} {result}')
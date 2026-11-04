
from collections import OrderedDict

def solution(cacheSize, cities):
    cache = OrderedDict()
    answer = 0

    for city in cities:
        key = city.lower()

        # 캐시 크기가 0이면 항상 Miss
        if cacheSize == 0:
            answer += 5
            continue

        if key in cache:
            # Cache Hit
            answer += 1
            cache.move_to_end(key)
        else:
            # Cache Miss
            answer += 5

            if len(cache) >= cacheSize:
                cache.popitem(last=False)

            cache[key] = True

    return answer

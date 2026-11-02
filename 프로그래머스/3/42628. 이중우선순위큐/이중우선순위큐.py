import heapq

def solution(operations):
    heap = []
    for op in operations:
        cmd = op.split()
        if cmd[0] == "I":
            heapq.heappush(heap, int(cmd[1]))
        if cmd[0] == "D":
            if cmd[1] == "1" and heap:
                heap.remove(max(heap))
                heapq.heapify(heap)
            elif cmd[1] == "-1" and heap:
                heapq.heappop(heap)

    if heap:
        return [max(heap), min(heap)]
    return [0, 0]
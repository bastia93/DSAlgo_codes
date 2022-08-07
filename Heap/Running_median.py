"""
given a stream of integers find the median at every index satring from 0.

example: [4,3,6,8,9,2,10]
output : [4,3.5,4,5, 6, 5, 6]

"""
from heapq import heapify, heappop, heappush


def solve(arr) -> list[int]:
    min_heap = []
    max_heap = []
    heapify(max_heap)
    heapify(min_heap)

    running_median = []

    n = len(arr)

    for i in range(n):
        if len(max_heap) == 0 or arr[i] <= -max_heap[0]:
            heappush(max_heap, -arr[i])

            if len(max_heap) - len(min_heap) > 1:
                heappush(min_heap, -heappop(max_heap))
        else:
            heappush(min_heap,arr[i])
            if len(min_heap) > len(max_heap):
                heappush(max_heap, -heappop(min_heap))

        if len(min_heap) == len(max_heap):
            running_median.append((min_heap[0] - max_heap[0])/2)
        else:
            running_median.append(-max_heap[0])

    return running_median

print(solve([4,3,6,8,9,2,10]))
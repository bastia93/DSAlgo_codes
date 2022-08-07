"""
You are given an array A containing N numbers.
This array is called special if it satisfies one of the following properties:

There exists an element A[i] in the array such that A[i] is equal
to the median of elements [A[0], A[1], ...., A[i-1]]

There exists an element A[i] in the array such that A[i] is equal
to the median of elements [A[i+1], A[i+2], ...., A[N-1]]

The Median is the middle element in the sorted list of elements.
If the number of elements is even then the median will be (sum of both middle elements) / 2.

Return 1 if the array is special else return 0.

For A[0] consider only the median of elements [A[1], A[2], ..., A[N-1]]
(as there are no elements to the left of it)
For A[N-1] consider only the median of elements [A[0], A[1], ...., A[N-2]]
"""
from heapq import heapify, heappop, heappush


def find_median(arr):
    n = len(arr)

    median_arr = [-99999999]

    max_heap = []
    min_heap = []
    heapify(max_heap)
    heapify(min_heap)

    # initialize the max_heap with the first element
    heappush(max_heap, -arr[0])

    for i in range(1, n):
        # Median Calculation for the current index

        if len(max_heap) == len(min_heap):
            median = (-max_heap[0] + min_heap[0]) / 2
        else:
            median = -max_heap[0]*1.0
        median_arr.append(median)

        # Now add the current element at the proper place

        if arr[i] <= -max_heap[0]:
            heappush(max_heap, -arr[i])

            if len(max_heap) - len(min_heap) > 1:
                heappush(min_heap, -heappop(max_heap))
        else:
            heappush(min_heap, arr[i])
            if len(min_heap) > len(max_heap):
                heappush(max_heap, -heappop(min_heap))

    return median_arr


def solve(A) -> list[int]:
    left_median = find_median(A)
    print("Left Median: ", left_median)
    right_median = find_median(A[::-1])[::-1]
    print("Right Median: ", right_median)

    A = [i*1.0 for i in A]
    n = len(A)

    print("A: ", A)
    for i in range(n):
        if A[i] == left_median[i] or A[i] == right_median[i]:
            return 1
    else:
        return 0


print(solve([ 4, 6, 8, 4 ]))
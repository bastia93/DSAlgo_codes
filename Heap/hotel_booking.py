"""
A hotel manager has to process N advance bookings of rooms for
 the next season. His hotel has K rooms.

Bookings contain an arrival date and a departure date.

He wants to find out whether there are enough rooms in the hotel to satisfy the demand.

"""


from heapq import heappop, heappush, heapify


def solve(arrive, depart, K):
    heap = []
    heapify(heap)
    count_guest = 0
    n = len(arrive)
    arr = [[arrive[i], depart[i]] for i in range(n)]
    arr.sort()
    for i in range(n):
        if count_guest < K:
            heappush(heap, arr[i][1])
            count_guest += 1
        else:
            temp = heappop(heap)
            if temp < arr[i][0]:
                heappush(heap, arr[i][1])
            else:
                return 0

    return 1


def method_2(arrive, depart, K):
    events = [(t, 1) for t in arrive] + [(t, 0) for t in depart]
    print(events)
    events = sorted(events)


    guests = 0

    for event in events:
        if event[1] == 1:
            guests += 1
        else:
            guests -= 1

        if guests > K:
            return 0

    return 1

# A = [ 13, 14, 36, 19, 44, 1, 45, 4, 48, 23, 32, 16, 37, 44, 47, 28, 8, 47, 4, 31, 25, 48, 49, 12, 7, 8 ]
# B = [ 28, 27, 61, 34, 73, 18, 50, 5, 86, 28, 34, 32, 75, 45, 68, 65, 35, 91, 13, 76, 60, 90, 67, 22, 51, 53 ]
# C = 23

# print(solve(A, B, C))

A = [1, 3, 5]
B = [2, 6, 8]
C = 1
print(method_2(A, B, C))
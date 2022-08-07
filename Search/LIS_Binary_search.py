
def binary_search(arr:list, target:int) -> int:
    start = 0
    end = len(arr) - 1

    while(start < end):
        mid = (start + end) //2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid
        else:
            return mid
    return start

def solve(A):
    temp_arr = [A[0]]
    length_LIS = 1
    n = len(A)

    for i in range(1, n):
        print("At the start of loop", temp_arr, "The element is: ", A[i])
        if A[i] > temp_arr[-1]:
            temp_arr.append(A[i])
            length_LIS += 1
        elif A[i] < temp_arr[0]:
            temp_arr[0] = A[i]
        elif temp_arr[0] < A[i] < temp_arr[-1]:
            index = binary_search(temp_arr, A[i])
            temp_arr[index] = A[i]
        #print("At the end of the loop: ", temp_arr)
    return length_LIS

A = [ 1, 9, 5, 10, 2, 3, 1, 7, 6 ]
print(solve(A))


"""
Question: in the binary search function
why it works when we write
end = mid
not end = mid -1
"""
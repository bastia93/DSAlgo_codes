def waterTrap(A):
    arrLength = len(A)
    left_max_arr = []
    right_max_arr = []

    # calculate left_max_arr
    left_max = -1
    for i in range(arrLength):
        left_max_arr.append(left_max)
        left_max = max(left_max, A[i])
    print(f"main arr:   {A}")
    print(f"left max arr: {left_max_arr}")
    # calculate right max arr
    right_max = -1
    for i in range(arrLength - 1, -1, -1):
        right_max_arr.append(right_max)
        right_max = max(right_max, A[i])
    right_max_arr = right_max_arr[::-1]
    print(f"rightmax arr: {right_max_arr}")
    ans = 0
    for i in range(arrLength):
        temp = min(left_max_arr[i], right_max_arr[i]) - A[i]
        if temp > 0:
            ans += temp

    return ans


A = [ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

temp = waterTrap(A)
print(temp)
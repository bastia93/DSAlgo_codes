def solve(A, B):
    n = len(A)
    m = len(B)
    if n < m:
        n, m = m, n
        A, B = B, A
    
    if m == 0:
        if n%2 == 0:
            mid = n//2
            return (A[mid] + A[mid-1])/2
        else:
            return A[n//2]



    total = n + m
    if total%2 == 0:
        left_side = total//2
    else:
        left_side = total//2 + 1
    

    l1= 0
    r1= 0
    l2= 0
    r2 = 0
    low = 0
    high = left_side

    while(low <= high):
        mid = (low+high)//2
        l1 = A[mid-1]
        r1 = A[mid]
        if left_side -mid > m:
            low = mid + 1
            continue
        if left_side - mid != 0:
            l2 = B[left_side - mid-1]
        else:
            l2 = -9999999

        if left_side - mid < m:
            r2 = B[left_side-mid]
        else:
            r2 = 99999999999

        #print("I am still printing")
        if l1 <= r2 and l2 <= r1:
            if total % 2 == 0:

                return (max(l1, l2) + min(r1, r2))/2
            else:
                return max(l1,l2)
        
        elif l1 > r2:
            high = mid-1
        else:
            low = mid + 1
    

A = [ -24, -11, -7, 4, 21, 26 ]
B = [ 25, 44 ]


print(solve(A,B))
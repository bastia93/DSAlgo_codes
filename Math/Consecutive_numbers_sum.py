
import math
def solve(A):
    count = 0
    k = 1
    special_num = ((k*(k-1))//2)
    #print("First Special",special_num)
    numerator = A - special_num
    
    while(numerator > 0):
        if numerator % k == 0:
            count += 1
        
        special_num += k
        k += 1
        #print(k, special_num)
        numerator = A - special_num
    
    return count

print(solve(90747))
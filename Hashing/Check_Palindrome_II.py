"""
Given a string A consisting of lowercase characters.

Check if characters of the given string can be rearranged 
to form a palindrome.

Return 1 if it is possible to rearrange the 
characters of the string A such that it becomes a
 palindrome else return 0.
"""

from itertools import count


def solve(A):
    n = len(A)
    hm = {}
    for i in A:
        if i not in hm:
            hm[i] = 0
        hm[i] += 1
    
    count_ones = 0
    for key, value in hm.items():
        if value % 2 != 0:
            count_ones += 1
    if n % 2 == 0:
        if count_ones == 0:
            return 1
        else:
            return 0
    else:
        if count_ones == 1:
            return 1
        else:
            return 0

print(solve("aaabb"))
        

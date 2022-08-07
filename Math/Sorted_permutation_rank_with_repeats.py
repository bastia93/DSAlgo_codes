"""
Given a string A, 
find the rank of the string amongst its permutations 
sorted lexicographically. 
Note that the characters might be repeated. 
If the characters are repeated, 
we need to look at the rank in unique permutations. 
Look at the example for more details.

NOTE:

The answer might not fit in an integer, 
so return your answer % 1000003 where 1000003 is a prime number.
String A can consist of both lowercase and uppercase letters. 
Characters with lesser ASCII values are considered smaller, 
i.e., 'a' > 'Z'.

"""

def solve(A):
    A.sort()
    return A

print(solve(["Z", "a", "C", "d", "A", "e"]))
print(ord("a"))
print(ord("A"))


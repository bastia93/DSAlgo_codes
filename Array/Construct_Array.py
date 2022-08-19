"""
Simba has an integer array of length A. Despite having insisted alot,
He is not ready to reveal the array to his friend Expert.
But now, he is ready to reveal some hints about the array and
challenges Expert to find the values of his hidden array.
The hints revealed are as follows:

The array is sorted by values in ascending order.
All the elements in the array are distinct and positive (greater than 0).
The array contains two elements B and C such that B < C.
Difference between all adjacent (consecutive) elements are equal.
Among all the arrays satisfying the above conditions,
his array has the minimum possible maximum element value.
If there are multiple possible arrays, his array will have
minimum possible minimum element value.
Can you help Expert to construct such an array and surprise Simba?

"""


def find_first_element(number, difference, max_diff):
    start_number = number
    number -= difference

    while number > 0 and max_diff > 0:
        start_number = number
        max_diff -= 1
        number -= difference

    return start_number


def solve(A, B, C):
    min_start = B
    final_diff = C-B
    min_last = B + final_diff * (A-1)
# for each difference between B and C
    for i in range(1, A):
        if (C-B)/i == ((C-B)//i * 1.0):
            diff = (C-B)//i
            temp_start = find_first_element(B, diff, A-1-i)
            temp_last = temp_start + (diff * (A-1))

            if C <= temp_last < min_last:
                min_last = temp_last
                min_start = temp_start
                final_diff = diff

    ans = []
    for i in range(A):
        ans.append(min_start + final_diff*i)

    return ans


print(solve(3, 1, 47))










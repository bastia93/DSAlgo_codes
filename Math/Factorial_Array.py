"""
Groot has an array A of size N. Boring, right? Groot thought so too, so he decided to construct another array B of the same size and defined elements of B as:

B[i] = factorial of A[i] for every i such that 1<= i <= N.

factorial of a number X denotes (1 x 2 x 3 x 4......(X-1) x (X)). Now Groot is interested in the total number of non-empty subsequences of array B such that every element in the subsequence has the same non-empty set of prime factors.

Since the number can be huge, return it modulo 109 + 7.

NOTE: A set is a data structure having only distinct elements. E.g : the set of prime factors of Y=12 will be {2,3} and not {2,2,3}

"""


def seive(x: int):
    prime = [True for i in range(x + 1)]
    p = 2
    while (p * p <= x):

        if prime[p]:
            for i in range(p * 2, x + 1, p):
                prime[i] = False
        p += 1

    prime_list = []
    for i in range(2, x + 1):
        if prime[i]:
            prime_list.append(i)

    return prime_list


def exponent_calculation(base,exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        return exponent_calculation(base * base, exponent//2)
    else:
        return base * exponent_calculation(base * base, exponent//2)


def solve(A):
    mod = 10 ** 9 + 7
    A = sorted(A)
    no_A = len(A)

    i = 0
    while A[i] == 1:
        i += 1

    A = A[i:]


    prime_numbers = seive(A[-1])

    no_A = len(A)
    no_prime = len(prime_numbers)

    if no_prime == 1:
        ans = exponent_calculation(2, no_A) - 1
        return ans % mod

    ans = 0

    point_to_A = 0

    point_to_prime = 1

    while (point_to_A < no_A and point_to_prime < no_prime):
        temp_count = 0
        while (A[point_to_A] < prime_numbers[point_to_prime]):
            point_to_A += 1
            temp_count += 1


        ans += exponent_calculation(2, temp_count) - 1
        point_to_prime += 1

    temp_count = no_A - point_to_A

    ans += (exponent_calculation(2, temp_count) - 1)

    return ans % mod


x = [ 251, 923, 561, 230, 100, 399, 542, 198, 548, 892, 721, 781, 174, 809, 9, 232, 165, 861, 36, 837, 377, 313, 475, 269, 210, 530, 940, 570, 24, 434, 764, 275, 709, 325, 505, 161, 724, 47, 359, 625, 291, 81, 406, 465, 242, 767, 698, 408, 629, 86, 597, 358, 399, 72, 979, 962, 603, 919, 884, 627, 353, 1, 254, 414, 678, 111, 575, 755, 511, 287, 380, 802, 720, 138, 620, 314, 905, 670, 74, 886, 756, 671, 244, 508, 744, 224, 822, 347, 495, 706, 326, 201, 707, 580, 615, 386, 43, 543, 141, 554 ]
print(sorted(x))
print(solve(x))

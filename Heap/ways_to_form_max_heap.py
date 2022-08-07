from math import log2


def solve(A):
    factorial = [1 for i in range(A + 1)]
    # Factorial calculation
    for i in range(1, A + 1):
        factorial[i] = factorial[i - 1] * i

    # Combination calculation
    def combination(n, r):
        numerator = factorial[n]
        denominator = factorial[n - r] * factorial[r]
        return numerator // denominator

    # Number of ways heap calculation
    def ways(n):
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            remaining_element = n - 1
            height = int(log2(n))
            x = 2**height - 1
            left_nodes = (x-1)//2 + min(n-x, (x+1)//2)
            right_nodes = remaining_element - left_nodes
            #print(f"left nodes: {left_nodes}")
            left_ways = ways(left_nodes)
            right_ways = ways(right_nodes)
            number_of_ways_to_choose = combination(remaining_element, left_nodes)
            #print(f"remain elements {remaining_element}, left child: {left_ways}, right chile: {right_ways}, ways selected: {number_of_ways_to_choose}")
            return left_ways * right_ways * number_of_ways_to_choose

    ans = ways(A) % (10 ** 9 + 7)
    return ans


print(solve(5))
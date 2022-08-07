def solve(A):
    mod = 10**9+7
    temp = power(3, A-2, mod)
    ans = (A%mod) * ((A-1) % mod) * temp

    return ans % mod

"""
the base is continously changed when when the exponent is even
when the exponent is odd that base is separated and multiplied with the answer.

"""
def power(base, exp, mod):
    ans = 1
    base = base % mod
    if base == 0:
        return 0
    while(exp > 0):
        if exp % 2 == 1:
            ans = (ans * base) % mod
            exp -= 1
        else:
            exp = exp//2
            base = (base * base) % mod

    return ans


ans = solve(39)

print(ans)

#212884953
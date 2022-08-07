def solve(n):
    gray_code = []

    for i in range(1<<n):
        gray_code.append(i^(i>>1))

    return gray_code

print(solve(4))

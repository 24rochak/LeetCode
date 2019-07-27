def judgeSquareSum(c: int) -> bool:
    """
        F E R M A T's   T H E O R E M
    Any positive number n is expressible as a sum of two squares
    if and only if the prime factorization of n,
    every prime of the form (4k+3)
    occurs an even number of times.
    In case, c itself is a prime number, it won't be divisible by any of the primes in [0, root(n)]
    Thus, we need to check if c can be expressed in the form of 4k+3. If so,
    we need to return a False value, indicating that this prime occurs an odd number(1) of times."""
    if c % 4 != 3:
        print("here")
        return False

    n = int(c ** 0.5) + 1
    for i in range(2, n):
        if c % i == 0 and i % 4 == 3:
            count = 0
            while c % i == 0:
                count += 1
                c /= i
            if count % 2 != 0:
                return False

    return True


c = 6
ans = judgeSquareSum(c)
print(ans)
'''
for i in range(100):
    ans = judgeSquareSum(i)
    if ans == True:
        print(i)
'''

def climbStairs(n: int) -> int:
    if n == 0 or n == 1 or n == 2:
        return n

    prev_2 = 1
    prev_1 = 2
    current = prev_2 + prev_1
    count = 3
    while count != n:
        prev_2 = prev_1
        prev_1 = current
        current = prev_2 + prev_1
        count += 1

    return current


n = 5
ans = climbStairs(n)
print(ans)

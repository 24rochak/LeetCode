def numSquares(n):
    """
    :type n: int
    :rtype: int
    """
    dp = [0]
    while len(dp) <= n:
        dp += min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,
    return dp[n]


n = 43
ans = numSquares(n)
print(ans)

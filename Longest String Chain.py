def longestStrChain(words):
    """
    :type words: List[str]
    :rtype: int
    """
    dp = {}
    for w in sorted(words, key=len):
        dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
    return max(dp.values())


words = ["kxbvnw", "uqjszp", "pmukt", "aai", "aaicwm", "mhkzelhyek", "cjv", "v", "uqjjspzpp", "aaim", "uqjjszp",
         "uqjjspzppd", "uqjjspzp", "aaicm", "pukt", "pvmukt", "dgdb", "aaicwbm", "mhkelhyek", "jv"]
print(longestStrChain(words))

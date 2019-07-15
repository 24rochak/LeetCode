def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)


'''def strStr( haystack: str, needle: str) -> int:
    def LPS(needle):
        j = 0
        i = 1
        m = len(needle)
        lps = [0] * m
        lps[0] = 0
        while i < m:
            if needle[i] != needle[j]:
                if j == 0:
                    lps[i] = j
                    i += 1
                else:
                    j = lps[j - 1]
            else:
                lps[i] = j + 1
                i += 1
                j += 1
        return lps

    if len(needle) == 0:
        return 0
    needle = list(needle)
    lps = LPS(needle)

    haystack = list(haystack)

    n = len(haystack)
    m = len(needle)

    j = 0
    i = 0
    while (i < n):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]

            else:
                i += 1
        if j == m:
            return i - m

    return -1'''

haystack = "hello"
needle = "bba"
ans = strStr(haystack, needle)
print(ans)

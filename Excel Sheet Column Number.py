def titleToNumber(s: str) -> int:
    if not s:
        return 0
    count = 0
    n = len(s) - 1
    for i in range(n + 1):
        print(s[i], ord(s[i]) - 64, 26 ** n, (ord(s[i]) - 64) * (26 ** n))
        count += (ord(s[i]) - 64) * (26 ** n)
        n -= 1

    return count


s = "BA"
print(titleToNumber(s))

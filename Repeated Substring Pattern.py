def repeatedSubstringPattern(s: str) -> bool:
    l = len(s)
    i = 1
    while (i <= l / 2):
        temp = s[:i]
        print(temp)
        n2 = len(temp)
        print(n2)
        if l % n2 == 0 and temp * int(l / n2) == s:
            return True
        i += 1
    return False


str = "abc"
ans = repeatedSubstringPattern(str)
print(ans)

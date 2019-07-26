def lengthOfLastWord(s: str) -> int:
    n = len(s)
    i = n - 1
    count = 0
    while i >= 0:
        if s[i] != ' ':
            count += 1
        elif s[i] == ' ' and count != 0:
            break
        i -= 1
    return count


s = "hello "
ans = lengthOfLastWord(s)
print(ans)

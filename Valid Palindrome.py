import sys

sys.setrecursionlimit(999999999)


def validPalindrome(s: str) -> bool:
    def is_pali_range(i, j):
        return all(s[k] == s[j - k + i] for k in range(i, j))

    for i in range(int(len(s) / 2)):
        if s[i] != s[~i]:
            j = len(s) - 1 - i
            return is_pali_range(i + 1, j) or is_pali_range(i, j - 1)
    return True


s = "abcdedcba"
print(s)
ans = validPalindrome(s)
print(ans)

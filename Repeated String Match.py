def repeatedStringMatch(A: str, B: str) -> int:
    from math import ceil
    i = ceil(len(B) / len(A))
    if B in A * i:
        return i
    elif B in A * (i + 1):
        return i + 1
    else:
        return -1


A = "abcd"
print(A * 2)
print(A * 3)
B = "cdabcdab"
ans = repeatedStringMatch(A, B)
print(ans)

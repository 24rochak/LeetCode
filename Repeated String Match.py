def repeatedStringMatch(A: str, B: str) -> int:
    '''The starting of B should be somewhere in A when A is as long as A or 2A. '''
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

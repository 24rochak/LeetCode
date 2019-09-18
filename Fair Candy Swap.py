def fairCandySwap(A, B):
    Sa, Sb = sum(A), sum(B)
    diff = (Sb - Sa) // 2
    setB = set(B)
    for x in A:
        if x + diff in setB:
            return [x, x + diff]


A = [1, 2, 5]
B = [2, 4]
ans = fairCandySwap(A, B)
print(ans)

def minDominoRotations(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    counts = [A[0]] if A[0] == B[0] else [A[0], B[0]]
    ans = len(A)
    for i in counts:
        c1 = c2 = 0
        for j in range(len(A)):
            if (A[j] != i) and (B[j] != i):
                break
            if (A[j] == i) and (B[j] == i):
                continue
            if A[j] == i:
                c1 += 1
            elif B[j] == i:
                c2 += 1
        if j == len(A) - 1:
            ans = min(ans, min(c1, c2))
    return ans if ans < len(A) else -1


A = [1, 2, 1, 1, 1, 2, 5, 2]
B = [2, 2, 2, 2, 2, 2, 3, 2]
ans = minDominoRotations(A, B)
print(ans)

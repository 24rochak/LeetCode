def addToArrayForm(A, K: int) -> [int]:
    a = "".join(str(i) for i in A)
    a = str(int(a) + k)
    return [a[i] for i in range(len(a))]


digits = [2, 7, 4]
k = 181
ans = addToArrayForm(digits, k)
print(ans)

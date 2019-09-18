def transpose(A):
    n = len(A)
    print(n)
    m = 1 if A[0] is not int else len(A[0])
    print(m)
    mat = [[None for _ in range(n)] for _ in range(m)]

    print(mat)

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(i, j)
            mat[i][j] = A[j][i]
    return mat


a = [0, 0, 0, 0]
ans = transpose(a)
print(ans)

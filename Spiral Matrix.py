def spiralOrder(matrix) -> [int]:
    nrows = len(matrix)
    ncols = len(matrix[0])
    print(nrows, ncols)

    count = 0
    i, j = 0, -1
    ans = []
    p = 0
    while count < nrows * ncols:
        for j in range(j + 1, ncols - p):
            ans.append(matrix[i][j])
            count += 1
        for i in range(i + 1, nrows - p):
            ans.append(matrix[i][j])
            count += 1
        for j in reversed(range(j - 1, p)):
            ans.append(matrix[i][j])
            count += 1
        for i in reversed(range(i - 1, p + 1)):
            ans.append(matrix[i][j])
            count += 1
        p += 1

        print(ans)

    return ans


mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

ans = spiralOrder(mat)
print(ans)

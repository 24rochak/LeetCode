def printDiagonal(mat):
    d = {}
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if (i + j) not in d:
                d[(i + j)] = []
            d[i + j].append(mat[i][j])
    ans = []

    for i in sorted(d.keys()):
        if i % 2 == 1:
            ans += d[i]
        else:
            ans += reversed(d[i])
    return ans


mat = [[1, 2, 3, 4, 5]]

print(printDiagonal(mat))

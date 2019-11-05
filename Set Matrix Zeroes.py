def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = []
    cols = []
    for i in range(len(matrix)):
        flag = 0
        for j in range(len(matrix[0])):
            print(i, j)
            if matrix[i][j] == 0:
                cols.append(j)
                flag = 1
        if flag:
            matrix[i][:] = [0] * (j + 1)

    '''for row in rows:
        matrix[row][:]=[0]*len(matrix[0])'''

    for i in range(len(matrix)):
        for col in cols:
            matrix[i][col] = 0

    return matrix


mat = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 0, 1, 5]
]


def test(mat):
    for i in range(len(mat[0])):
        min = mat[0][i]
        for j in range(len(mat)):
            print(mat[j][i])

        print(min)


test(mat)

mat = setZeroes(mat)

for row in mat:
    print(row)

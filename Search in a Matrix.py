def searchMatrix(matrix, target):
    while len(matrix) > 0 and len(matrix[0]) > 0:
        if matrix == [[]]:
            return False
        print("here")
        print(matrix)
        if matrix[0][-1] == target:
            return True
        elif matrix[0][-1] > target:
            print("column")
            for row in matrix:
                del row[-1]
        elif matrix[0][-1] < target:
            print("row")
            del matrix[0]
    return False


def delete_col(mat):
    for i in range(len(mat)):
        del mat[i][-1]

    print(mat)


mat = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]

mat = [[1], [2], [3], [4]]
mat = [[-1], [-1]]

# delete_col(mat)
print(searchMatrix(mat, 20))

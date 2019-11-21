def uniquePathsWithObstacles(matrix):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    if matrix[0][0] == 1 or matrix[-1][-1] == 1:
        return 0

    matrix[0][0] = 1
    for i in range(1, len(matrix)):
        if not matrix[i][0]:
            matrix[i][0] = matrix[i - 1][0]
        else:
            matrix[i][0] = 0

    for i in range(1, len(matrix[0])):
        if not matrix[0][i]:
            matrix[0][i] = matrix[0][i - 1]
        else:
            matrix[0][i] = 0

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            matrix[i][j] = int(not matrix[i][j])

            if matrix[i][j] == 1:
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
            else:
                matrix[i][j] = 0
    for row in matrix:
        print(row)
    return matrix[-1][-1]


grid = [[0, 1, 0]]
print(uniquePathsWithObstacles(grid))
